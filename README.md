# Removing Background with Python

## Prerequisites

### Installing GCC, BLAS e LPAK

These dependencies must be installed at operational system level. They will be used by torchvision to apply the calcs for needed for background removing algorithm.

```
$ brew install gcc
$ brew install openblas
$ brew install lapack
```

## Python Dependencies

### Create a enviroment to execute

Just to create a isolated environement for developing.

```
$ python3 -m venv gbtest
$ cd gbtest
$ source ./bin/activate
```

### Installing Numpy

Needed for the buffer transformation of the file to rembg lib.

```
$ pip install numpy
```

### Installing torchvision

The main algorithm for removal looks to be part of this lib.

``````
$ pip install torchvision
``````

### Installing Pillow

Pillow is just for generating an image to save to disk. Maybe we could send the bytes to a client.

```
$ python3 -m pip install --upgrade pip
$ python3 -m pip install --upgrade Pillow
```

### Installing FastApi

I've used FastApi because it was new to me and looks simple to expose a endpoint to upload file.

```
$ pip install fastapi
$ pip install uvicorn
```

## Executing the App

### Running the server

From the src dir inside the env, execute:

```
$ uvicorn server:app --reload
```

### Route for Upload

```
POST http://localhost:8000/upload
- file: bytes
```

