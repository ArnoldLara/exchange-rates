FROM python:3
COPY web_rates web_rates
RUN pip install --no-cache-dir -r web_rates/requirements.txt
EXPOSE 5000
#CMD cat web_rates/app.py
#CMD pip show requests
#CMD [ "python", "web_rates/app.py" ]
CMD python3 web_rates/app.py