FROM python:3.7-slim

RUN python3.7 -m pip install pip

WORKDIR /mini-project
RUN pip install flask && pip install pytest
RUN pip install websockets
RUN pip install tzwhere
RUN pip install pytz
RUN pip install pandas
RUN pip install numpy
RUN pip install timezonefinder

COPY Controllers_1_0 /mini-project/Controllers_1_0
COPY Tests /mini-project/Tests
COPY utils /mini-project/utils
COPY Websocket_1_0 /mini-project/Websocket_1_0
COPY app.py /mini-project/app.py
COPY config.py /mini-project/config.py
COPY startup.py /mini-project/startup.py
COPY Input_csv_files/timezone.csv /mini-project/timezone.csv

ENTRYPOINT ["python"]