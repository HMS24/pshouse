**Show Deals**
----
實價登錄列表

- **URL:** `/apiv1/deals`
- **Method:** `GET` 
- **URL Params:**

    - **Required:**

        None

    - **Optional**

        - `city=[str]`<br />
            default: `新北市`
        - `district=[str]`<br />
            default: `淡水區`
        - `from_=[int]`<br />
            default: `距今一年前 timestamp`
        - `to_=[int]`<br />
            default: `datetime.now() timestamp`
        - `search=[str]`<br />
        - `start=[int]`<br />
            default: `0`
        - `length=[int]`<br />
            default: `15`
        - `sort=[str]`<br />
            default: `-transaction_date` <br />
            sortable: `transaction_date`, `price` and `unit_price` <br />
            order: `+` 代表 asc  `-` 代表 desc 

- **Data Params**

    None

- **Success Response:**

  - **Code:** 200 <br />
    **Content:**
    ```json
    {
        "result": {
            "data": [
                {
                    "bathroom": 1,
                    "build_name": "金城舞 世界花園",
                    "building_state": "住宅大樓(11層含以上有電梯)",
                    "building_total_area": 89.98,
                    "buildings": "B03棟24號",
                    "city": "新北市",
                    "created_at": "2022-01-01T00:00:00",
                    "district": "土城區",
                    "id": 5334,
                    "land_total_area": 9.85,
                    "level": "二十四層",
                    "location": "新北市土城區莊園街",
                    "main_use": "住家用",
                    "note": "",
                    "object_of_transaction": "房地(土地+建物)+車位",
                    "parking_sapce_price": 2300000,
                    "parking_sapce_total_area": 18.4,
                    "parking_sapce_type": "坡道平面",
                    "price": 14050000,
                    "restaurant_and_living_room": 1,
                    "room": 3,
                    "total_floor_numbers": "24",
                    "transaction_date": "2022-07-28",
                    "unit_price": 164152,
                    "updated_at": "2022-09-01T13:22:56"
                },
            ],
            "total": 10
        }
    }
    ```
 
- **Error Response:**

    None

- **Sample Call:**

  ```javascript
    $.ajax({
      url: "/apiv1/deals",
      dataType: "json",
      type: "GET",
      success: res => console.log(res)
    });
  ```