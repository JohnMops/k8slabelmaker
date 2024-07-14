FROM python:3.12.4

COPY --chown=${LOCAL_USER}:${LOCAL_USER} source /home/${LOCAL_USER}/source
COPY --chown=${LOCAL_USER}:${LOCAL_USER} images/${SERVICE_NAME}/entrypoint.sh /home/${LOCAL_USER}/entrypoint.sh

RUN chmod a+x /home/${LOCAL_USER}/entrypoint.sh && \
    pip install --no-cache-dir -r /home/${LOCAL_USER}/source/requirements.txt

ENTRYPOINT ["/home/run-user/entrypoint.sh"]