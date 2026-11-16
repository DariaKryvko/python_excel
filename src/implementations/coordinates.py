def coords_to_cell_id(row: int, col: int) -> str:
    """Convert 0-based row and col to A1 notation (e.g. 0, 0 -> A1)."""
    col_str = ""
    n = col
    while n >= 0:
        col_str = chr(ord("A") + (n % 26)) + col_str
        n = n // 26 - 1
    return f"{col_str}{row + 1}"

def cell_id_to_coords(cell_id: str) -> tuple[int, int]:
    """Convert A1 notation to 0-based (row, col) (e.g. A1 -> (0, 0))."""
    cell_id = cell_id.strip().upper()
    col_part = ""
    row_part = ""
    for ch in cell_id:
        if ch.isalpha():
            col_part += ch
        elif ch.isdigit():
            row_part += ch
    if not col_part or not row_part:
        raise ValueError(f"Invalid cell identifier: {cell_id}")
    col = 0
    for ch in col_part:
        col = col * 26 + (ord(ch) - ord("A") + 1)
    col -= 1
    row = int(row_part) - 1
    return (row, col)

