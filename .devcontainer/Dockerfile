FROM espressif/idf:v6.0.1

# Get the host user's UID and GID (passed as build args)
ARG USERNAME=developer
ARG USER_UID=1000
ARG USER_GID=1000

# Create user with same UID/GID as host
RUN if getent group $USER_GID; then groupmod -n $USERNAME $(getent group $USER_GID | cut -d: -f1); else groupadd --gid $USER_GID $USERNAME; fi \
    && if getent passwd $USER_UID; then usermod -l $USERNAME -m -d /home/$USERNAME $(getent passwd $USER_UID | cut -d: -f1); else useradd --uid $USER_UID --gid $USER_GID -m $USERNAME; fi \
    && apt-get update \
    && apt-get install -y sudo \
    && echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME \
    && chmod 0440 /etc/sudoers.d/$USERNAME

# Install clangd-22
RUN wget -qO- https://apt.llvm.org/llvm-snapshot.gpg.key | tee /etc/apt/trusted.gpg.d/apt.llvm.org.asc && \
    echo "deb http://apt.llvm.org/noble/ llvm-toolchain-noble-22 main" > /etc/apt/sources.list.d/llvm.list && \
    apt-get update && \
    apt-get install -y clangd-22 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Setup bashrc for the user
RUN echo "source /opt/esp/idf/export.sh" >> /home/$USERNAME/.bashrc

# Switch to the user
USER $USERNAME
