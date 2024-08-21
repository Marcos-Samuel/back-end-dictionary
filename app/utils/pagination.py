from typing import List, Dict

def paginate(items: List[Dict], page: int, limit: int) -> Dict:
    start = (page - 1) * limit
    end = start + limit
    paginated_items = items[start:end]
    total_items = len(items)
    total_pages = (total_items + limit - 1)
    return {
        "results": paginated_items,
        "totalDocs": total_items,
        "page": page,
        "totalPages": total_pages,
        "hasNext": page < total_pages,
        "hasPrev": page > 1
    }
