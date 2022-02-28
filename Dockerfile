FROM python:3.8
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./
RUN python setup.py install
EXPOSE 8501
ENTRYPOINT ["streamlit", "run"]
CMD ["./streamlit_front/streamlit_main.py"]
