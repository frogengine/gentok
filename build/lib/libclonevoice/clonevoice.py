from elevenlabs import clone, generate, play
from elevenlabs import set_api_key
import os

set_api_key("a3855ad0815f121c6eeae907349c65f0")

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