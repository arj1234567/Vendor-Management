# Vendor-Management
## API Endpoint: /api/vendor/
### Description:
POST: Create a new vendor.
GET: List all vendors.
### Method:
POST: POST
GET: GET
### Parameters:
None
### Request Body:
For POST:
{
   "Name": "Vendor Name",
   "Contact_details": "Vendor Contact Details",
   "Address": "Vendor Address",
   "Vendor_code": "Unique Vendor Code"
    "On_time_delivery":"ontime delivery"
    "Quality_rating_average":"quality_average"
    "Average_response_time": "average_response"
    "Fullfillment_rate":"fullfillment_rate"
}
### Response:
Success Response:
Code: 201
Content:
{
   "status": "success",
   "data": {
      "Name": "Vendor Name",
      "Contact_details": "Vendor Contact Details",
      "Address": "Vendor Address",
      "Vendor_code": "Unique Vendor Code"
      "On_time_delivery":"ontime delivery"
      "Quality_rating_average":"quality_average"
      "Average_response_time": "average_response"
      "Fullfillment_rate":"fullfillment_rate"
   }
}
## Error Response:
Code: 400
Content:
{
   "status": "error",
   "data": "Error message"
}
## API Endpoint: /api/vendor/{id}
### Description:
GET: Retrieve details of a specific vendor.
PUT: Update a vendor's details.
DELETE: Delete a vendor.
### Method:
GET: GET
PUT: PUT
DELETE: DELETE
### Parameters:
id: Integer - Unique identifier for the vendor.
### Request Body:
For PUT:
{
   "Name": "Updated Vendor Name",
   "Contact_details": "Updated Vendor Contact Details",
   "Address": "Updated Vendor Address",
   "Vendor_code": "Updated Unique Vendor Code"
    "On_time_delivery":"Updated ontime delivery"
    "Quality_rating_average":"Updated quality_average"
    "Average_response_time": "Updated average_response"
    "Fullfillment_rate":"Updated fullfillment_rate"
}
### Response:
Success Response:
Code: 200
Content:
{
   "status": "success",
   "data": {
     "Name": "Updated Vendor Name",
   "Contact_details": "Updated Vendor Contact Details",
   "Address": "Updated Vendor Address",
   "Vendor_code": "Updated Unique Vendor Code"
    "On_time_delivery":"Updated ontime delivery"
    "Quality_rating_average":"Updated quality_average"
    "Average_response_time": "Updated average_response"
    "Fullfillment_rate":"Updated fullfillment_rate"
   }
}
### Error Response:
Code: 400
Content:
{
   "status": "error",
   "data": "Error message"
}
### Sample Request:
GET: /api/vendor/1
### Sample Response:
Success Response:
Content:
{
   "status": "success",
   "data": {
       "id":"1"
      "Name": "Vendor Name",
      "Contact_details": "Vendor Contact Details",
      "Address": "Vendor Address",
      "Vendor_code": "Unique Vendor Code"
      "On_time_delivery":"ontime delivery"
      "Quality_rating_average":"quality_average"
      "Average_response_time": "average_response"
      "Fullfillment_rate":"fullfillment_rate"
   }
}
### Error Response:
{
   "status": "error",
   "data": "Error message"
}
## API Endpoint: /api/purchase/
### Description:
POST: Create a new purchase order.
GET: List all purchase orders.
### Method:
POST: POST
GET: GET
### Parameters:
None
### Request Body:
For POST:
{
   "Po_number": "PO Number",
   "Vendor_id": "Vendor ID",
   "Order_date": "Order Date",
   "Delivery_date": "Delivery Date",
   "Items": "Items Details",
   "Quantity": "Quantity",
   "Status": "Status"
    "Quality_rating":"quality_rating"
    "Issue_date":"issue_date"
    "Acknowledgement_rate":"acknowledgement_date"
}
### Response:
Success Response:
Code: 201
Content:
{
   "status": "success",
   "data": {
      "Po_number": "PO Number",
     "Vendor_id": "Vendor ID",
     "Order_date": "Order Date",
     "Delivery_date": "Delivery Date",
     "Items": "Items Details",
     "Quantity": "Quantity",
     "Status": "Status"
      "Quality_rating":"quality_rating"
      "Issue_date":"issue_date"
      "Acknowledgement_rate":"acknowledgement_date"
   }
}
### Error Response:
Code: 400
Content:
{
   "status": "error",
   "data": "Error message"
}
## API Endpoint: /api/purchase/{id}
### Description:
GET: Retrieve details of a specific purchase order.
PUT: Update a purchase order.
DELETE: Delete a purchase order.
### Method:
GET: GET
PUT: PUT
DELETE: DELETE
### Parameters:
id: Integer - Unique identifier for the purchase order.
Request Body:
For PUT:
{
   "Po_number": "Updated PO Number",
   "Vendor_id": "Updated Vendor ID",
   "Order_date": "Updated Order Date",
   "Delivery_date": "Updated Delivery Date",
   "Items": "Updated Items Details",
   "Quantity": "Updated Quantity",
   "Status": "Updated Status"
    "Quality_rating":"Updated quality_rating"
    "Issue_date":"Updated issue_date"
    "Acknowledgement_rate":"Updated acknowledgement_date"
}
### Response:
Success Response:
Code: 200
Content:
{
   "status": "success",
   "data": {
     "Po_number": "Updated PO Number",
     "Vendor_id": "Updated Vendor ID",
     "Order_date": "Updated Order Date",
     "Delivery_date": "Updated Delivery Date",
     "Items": "Updated Items Details",
     "Quantity": "Updated Quantity",
     "Status": "Updated Status"
     "Quality_rating":"Updated quality_rating"
     "Issue_date":"Updated issue_date"
     "Acknowledgement_rate":"Updated acknowledgement_date"
   }
}
### Error Response:
Code: 400
Content:
{
   "status": "error",
   "data": "Error message"
}
### Sample Request:
GET: /api/purchase/1
Sample Response:
Success Response:
{
   "status": "success",
   "data": {
       "Po_number": "PO Number",
       "Vendor_id": "Vendor ID",
       "Order_date": "Order Date",
       "Delivery_date": "Delivery Date",
        "Items": "Items Details",
       "Quantity": "Quantity",
       "Status": "Status"
       "Quality_rating":"quality_rating"
       "Issue_date":"issue_date"
       "Acknowledgement_rate":"acknowledgement_date"
   }
}
### Error Responses:
Error Response:
{
   "status": "error",
   "data": "Error message"
}
## API Endpoint: /api/vendor/{vendor_id}/performance/
### Description:
GET: Retrieve performance metrics for a specific vendor.
### Method:
GET: GET
### Parameters:
vendor_id: Integer - Unique identifier for the vendor.
### Request Body:
None
### Response:
Success Response:
Code: 200
Content:
{
   "on_time_delivery_rate": "On-Time Delivery Rate",
   "quality_rating_avg": "Quality Rating Average",
   "average_response_time": "Average Response Time",
   "fulfillment_rate": "Fulfillment Rate"
}
### Error Response:
Code: 400
Content:
{
   "status": "error",
   "data": "Error message"
}
## API Endpoint: /api/purchase_orders/{id}/acknowledge/
### Description:
POST: Acknowledge a purchase order.
### Method:
POST: POST
### Parameters:
id: Integer - Unique identifier for the purchase order.
### Request Body:
None
### Response:
Success Response:
Code: 200
Content:
{
   "status": "success",
   "message": "Purchase order acknowledged successfully",
   "avg_response_time": "Average Response Time"
}
### Error Responses:
Error Response:
{
   "status": "error",
   "data": "Error message"
}
