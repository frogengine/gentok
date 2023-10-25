from elevenlabs import clone, generate, play
from elevenlabs import set_api_key
import os

set_api_key("a74699ff20ccb863ffde7dea636c0c81")

def clonevoice(txt: str, sample: str):

    filename = sample
    #filename = os.path.join( os.path.dirname( __file__ ), filename )
    voice = clone(
        name="Alex",
        description="An old American male voice with a slight hoarseness in his throat. Perfect for news", # Optional
        files=[filename],
    )

    audio = generate(text=txt, voice=voice)

    play(audio)

from elevenlabs import clone, generate, play

clonevoice("hello seungnock","D:\workspace\python\gentoklibs\sample-5.mp3")