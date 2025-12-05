import re
def inclusive_range_from_string(r_str: str):
    if not isinstance(r_str, str):
        raise TypeError(f'{type(r_str)} should be str')
    r_str_split = list(map(lambda x: int(x), r_str.split('-')))
    if len(r_str_split) != 2:
        raise ValueError(f'range {r_str} is not valid')
    r_str_split[1] += 1
    return [i for i in range(*r_str_split)]

def validate_id(p_id):
    pattern = r'^(\d+)\1+$'
    return not re.search(pattern, str(p_id))