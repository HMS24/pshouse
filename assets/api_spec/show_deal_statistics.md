**Show Deal Statistics**
----
實價登錄列表

- **URL:** `/apiv1/deal-statistics`
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
            "data": [
                {
                "avg_house_price": 748,
                "avg_house_unit_price": 27,
                "avg_total_price": 898,
                "build_name": "Park189",
                "city": "新北市",
                "created_at": "2022-09-19T14:07:23",
                "district": "淡水區",
                "id": 1,
                "month": "1",
                "room": 2,
                "updated_at": "2022-09-19T14:07:23",
                "year": "2022"
                },
            ],
            "total": 181
        }
    }
    ```
 
- **Error Response:**

    None

- **Sample Call:**

  ```javascript
    $.ajax({
      url: "/apiv1/deal-statistics",
      dataType: "json",
      type: "GET",
      success: res => console.log(res)
    });
  ```