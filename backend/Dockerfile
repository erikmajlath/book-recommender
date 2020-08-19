FROM python
WORKDIR /work
RUN pip install streamlit

ADD ./backend /work
ADD ./notebooks/data /data

EXPOSE 8501

CMD streamlit run app.py --server.port 8501