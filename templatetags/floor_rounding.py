from django import template

register = template.Library()

@register.filter
def round_down(total_count,nearest_value):
    total_count_int = int(total_count)
    nearest_value_int = int(nearest_value)
    
    original_divide_value = total_count_int/nearest_value_int
    rounded_divide_value = total_count_int//nearest_value_int
    
    rounded_count = rounded_divide_value * nearest_value_int
    
    if rounded_count > 0  and original_divide_value > rounded_divide_value:
        return f"{rounded_count}+"
    
    return str(total_count)

