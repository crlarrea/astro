FROM astrocrpublic.azurecr.io/runtime:3.1-1

# replace dbt-postgres with another supported adapter if you're using a different warehouse type
RUN python3 -m venv dbt_venv && source dbt_venv/bin/activate && \
    pip3 install --no-cache-dir dbt-postgres && deactivate