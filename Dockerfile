FROM langchain/langgraph-api:3.13

# Add constraints file
COPY api/constraints.txt /api/constraints.txt

# Add your assistant code
ADD . /deps/Bokrah-Ai-Assistant

# Install dependencies
RUN PYTHONDONTWRITEBYTECODE=1 pip install --no-cache-dir -c /api/constraints.txt -e /deps/Bokrah-Ai-Assistant

ENV LANGSERVE_GRAPHS='{"Bokrah Ai": "graph.build_graph:graph"}'

# Ensure user deps didn't inadvertently overwrite langgraph-api
RUN mkdir -p /api/langgraph_api /api/langgraph_runtime /api/langgraph_license && \
    touch /api/langgraph_api/__init__.py /api/langgraph_runtime/__init__.py /api/langgraph_license/__init__.py

RUN PYTHONDONTWRITEBYTECODE=1 pip install --no-cache-dir --no-deps -e /api

# Remove pip and build tools
RUN pip uninstall -y pip setuptools wheel && \
    rm -rf /usr/local/lib/python*/site-packages/pip* /usr/local/lib/python*/site-packages/setuptools* /usr/local/lib/python*/site-packages/wheel* && \
    find /usr/local/bin -name "pip*" -delete

WORKDIR /deps/Bokrah-Ai-Assistant
