import whisper, os
# The `load_model` function checks the cache and downloads
# if nothing is found. As this is used in the build process,
# the model will not be in the cache yet but it will
# be downloaded into the container.
# This could arguably even cached on the build system
# but I will leave it like this for now.
# The consuming container can then later (at runtime)
# call the `load_model` function again and the model
# will already be present in the cache
# # tldr
# we download at build time so the resulting
# container does not need internet access to download the model
# at runtime
model: str
try:
    model = os.environ["WHISPER_MODEL"]
except:
    model = "base"
whisper.load_model(model)
