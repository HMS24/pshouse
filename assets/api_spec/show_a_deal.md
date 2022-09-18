**Show A Deal**
----
單筆實價登錄 json 格式

- **URL:** `/apiv1/deals/:id`
- **Method:** `GET` 
- **URL Params:**

    - **Required:**

        None

    - **Optional**

        None

- **Data Params**

    None

- **Success Response:**

    - **Code:** 200 <br />
      **Content:**
        ```json
        {
            "result": {
                "bathroom": 2,
                "build_name": "勝旺興",
                "building_state": "住宅大樓(11層含以上有電梯)",
                "building_total_area": 147.47,
                "buildings": "B1棟2號",
                "city": "新北市",
                "created_at": "2022-01-01T00:00:00",
                "district": "新莊區",
                "id": 2,
                "land_total_area": 16.92,
                "level": "二層",
                "location": "新北市新莊區榮華路一段",
                "main_use": "住家用",
                "note": "",
                "object_of_transaction": "房地(土地+建物)+車位",
                "parking_sapce_price": 2300000,
                "parking_sapce_total_area": 25.64,
                "parking_sapce_type": "坡道平面",
                "price": 20500000,
                "restaurant_and_living_room": 2,
                "room": 3,
                "total_floor_numbers": "15",
                "transaction_date": "2021-11-13",
                "unit_price": 149388,
                "updated_at": "2022-09-01T13:22:55"
            }
        }
        ```
 
- **Error Response:**

    - **Code:** 404 <br />
      **Content:**
        ```json
        {
            "error": "Not Found",
            "message": "Deal id 9 doesn't exist."
        }
        ```

- **Sample Call:**

  ```javascript
    $.ajax({
      url: "/apiv1/deals/1",
      dataType: "json",
      type: "GET",
      success: res => console.log(res)
    });
  ```