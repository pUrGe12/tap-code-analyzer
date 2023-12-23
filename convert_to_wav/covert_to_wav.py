from pydub import AudioSegment

src = "" # enter mp3 file source here
dst = "" # enter destination of output file here (along with name)

sound = AudioSegment.from_mp3(src)
sound.export(dst, format="wav")