import pandas as pd
from typing import Dict, Any

class FilterEngine:
    """Handle all filtering operations"""

    @staticmethod
    def apply_filters(df: pd.DataFrame, global_search: str,
                      basic_filters: Dict[str, Any],
                      advanced_filters: Dict[str, Dict[str, str]]) -> pd.DataFrame:
        """Apply all filters to dataframe"""
        filtered_df = df.copy()

        # Apply global search
        if global_search:
            search_mask = df.astype(str).apply(
                lambda x: x.str.contains(global_search, case=False, na=False)
            ).any(axis=1)
            filtered_df = filtered_df[search_mask]

        # Apply basic filters (multiselect values)
        filtered_df = FilterEngine._apply_basic_filters(filtered_df, basic_filters)

        # Apply advanced filters (with operators)
        filtered_df = FilterEngine._apply_advanced_filters(filtered_df, advanced_filters)

        return filtered_df

    @staticmethod
    def _apply_basic_filters(df: pd.DataFrame, filters: Dict[str, Any]) -> pd.DataFrame:
        """Apply basic column filters"""
        filtered_df = df.copy()

        for col, filter_value in filters.items():
            if filter_value and col in filtered_df.columns:
                if isinstance(filter_value, list) and filter_value:
                    filtered_df = filtered_df[filtered_df[col].isin(filter_value)]

        return filtered_df

    @staticmethod
    def _apply_advanced_filters(df: pd.DataFrame, filters: Dict[str, Dict[str, str]]) -> pd.DataFrame:
        """Apply advanced column filters with operators"""
        filtered_df = df.copy()

        for col, filter_config in filters.items():
            if col in filtered_df.columns and filter_config.get('value'):
                value = filter_config['value']
                operator = filter_config.get('operator', 'contains')

                # Handle different value types
                if isinstance(value, list) and value:
                    filtered_df = filtered_df[filtered_df[col].isin(value)]
                elif isinstance(value, str) and value.strip():
                    mask = FilterEngine._get_operator_mask(filtered_df[col], operator, value)
                    filtered_df = filtered_df[mask]

        return filtered_df

    @staticmethod
    def _get_operator_mask(series: pd.Series, operator: str, value: str) -> pd.Series:
        """Get boolean mask for operator"""
        col_series = series.astype(str)

        operator_map = {
            'contains': lambda: col_series.str.contains(value, case=False, na=False),
            'equals': lambda: col_series.str.lower() == value.lower(),
            'starts_with': lambda: col_series.str.startswith(value, na=False),
            'ends_with': lambda: col_series.str.endswith(value, na=False),
            'not_contains': lambda: ~col_series.str.contains(value, case=False, na=False)
        }

        return operator_map.get(operator, operator_map['contains'])()
