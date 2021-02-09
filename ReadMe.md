## File Structure
mini-project <br />
├── Controllers_1_0 <br />
│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── __init__.py <br />
│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└── time_converter_controller.py <br />
├── Input_csv_files <br />
│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── timezone.csv <br />
│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└── timezone_modified.csv<br />
├── Tests <br />
│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── __init__.py <br />
│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└── time_converter_controller.py <br />
├── utils <br />
│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── csv_file_parser.py <br />
│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── distance_measurement.py <br />
│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└── timezone_converter_utils.py <br />
├── Websocket_1_0 <br />
│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── distance_measurement_websocket.py <br />
│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└── live_measurement_websocket.py <br />
├── app.py <br />
├── config.py <br />
├── Dockerfile <br />
└── startup.py <br />

## How to run program?
### From Docker Image
### Get Image from "docker pull skynapier/mini-project:1.0"

### command
docker run --name mini-project -d -p 5000:5000 mini-project ./app.py

docker run --name mini-project -d -p 5000:5000 skynapier/mini-project:1.0 ./app.py

docker build -t mini_project .

docker save --output C:\Users\skynapier\Desktop\mini-project\mini-project.tar mini-project



## Restful API
### GET all
127.0.0.1:5000/api/1.0/time-converter/all
![](Sample_output_images/get_all.png)

### GET by id
127.0.0.1:5000/api/1.0/time-converter/73k
![](Sample_output_images/get_id.png)

### POST 
#### Post ADD id not exist
127.0.0.1:5000/api/1.0/time-converter/add/?id=1&lat=-33.865143&lng=151.209900&timestamp=1480933800
![](Sample_output_images/post_add_successful.png)

#### Post ADD id exist
127.0.0.1:5000/api/1.0/time-converter/add/?id=1&lat=-33.865143&lng=151.209900&timestamp=1480933800
![](Sample_output_images/post_add_fail.png)

### PUT 
#### PUT update with id  exist
127.0.0.1:5000/api/1.0/time-converter/0/?lat=-33.865143&lng=151.209900&timestamp=1480933800
![](Sample_output_images/put_update_successful.png)

#### PUT update with id not exist
127.0.0.1:5000/api/1.0/time-converter/99/?lat=-33.865143&lng=151.209900&timestamp=1480933800
![](Sample_output_images/put_create_successful.png)

### Delete 

#### Delete successful
127.0.0.1:5000/api/1.0/time-converter/0
![](Sample_output_images/delete_successful.png)

#### Delete fail
127.0.0.1:5000/api/1.0/time-converter/9527
![](Sample_output_images/delete_fail.png)


