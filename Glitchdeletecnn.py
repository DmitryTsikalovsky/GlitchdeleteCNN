import loadmodule
import savemodule

def main():
    image_array = loadmodule.load_image()
    savemodule.save_image(image_array)

if __name__== "__main__":
    main()
