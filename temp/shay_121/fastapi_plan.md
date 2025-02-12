Related notes: https://l2c.northcoders.com/courses/de-notes/de2-backend-servers#sectionId=fastapi,step=intro

# Test for query:

```py
 expected_response = {
        "restaurants": [
            {
                "restaurant_id": 1,
                "restaurant_name": "Luck Lust Liquor & Burn",
                "area_name": "Northern Quarter",
                "cuisine": "Mexican",
                "website": "http://lucklustliquorburn.com/",
            },
            {
                "restaurant_id": 4,
                "restaurant_name": "This & That",
                "area_name": "Northern Quarter",
                "cuisine": "Family Run Indian Curryhouse",
                "website": "http://www.thisandthatcafe.co.uk/",
            },
            {
                "restaurant_id": 5,
                "restaurant_name": "Pieminister",
                "area_name": "Northern Quarter",
                "cuisine": "Pies And More Pies",
                "website": "",
            },
            {
                "restaurant_id": 7,
                "restaurant_name": "Dehli 2 go",
                "area_name": "Northern Quarter",
                "cuisine": "Late night food",
                "website": "http://delhi2go-online.co.uk/",
            },
        ]
    }
    response = client.get("/api/restaurants?area_name=Northern Quarter")
    assert response.status_code == 200
    assert response.json() == expected_response
```

# Implementing optional query:

Docs: https://fastapi.tiangolo.com/tutorial/query-params/?h=quer

FastAPI Queries:

```py
def get_restaurants(area_name: str | None = None):
```

Filtering logic with SQL:

```py
if area_name:
        sql_str += " WHERE area_name = :area_name"
        rows = conn.run(sql_str, area_name=area_name)
    else:
        rows = conn.run(sql_str)
```
