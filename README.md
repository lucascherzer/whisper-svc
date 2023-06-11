# whisper-svc

A containerization of OpenAIs whisper speech recognition model

## Building + Deploying

```sh
# Build
git clone https://github.com/lucascherzer/whisper-svc.git
cd whisper-svc
docker build -t whisper-svc .
# Deploy
docker run -p 5000:5000 whisper-svc
```
Note that the whisper model used by default is the `base` model.
This can be changed either at build or runtime, although changing at runtime has some
drawbacks, namely that the container can not guarantee that the model is downloaded at build time
so it will need internet access at runtime.

- To change at build time, add the flag `--build-arg WHISPER_MODEL=<model>` to the `docker build` command.
- To change at runtime, add the flag `--env WHISPER_MODEL=<model>` to the `docker run` command.

## API
The container exposes an API on port 5000, with only one endpoint:

### POST `/api/transcribe`
Accepts mp3 files in the body. The files will are run through the model.
Returns a JSON object:
```json
{
  "language": "lang",
  "text": "text"
}
```
The list of all possible languages is defined [here](https://github.com/openai/whisper/blob/248b6cb124225dd263bb9bd32d060b6517e067f8/whisper/tokenizer.py#L10)
