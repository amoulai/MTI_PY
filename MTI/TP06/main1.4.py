class Story:
    """
      Represent the complex object under construction.
    """

    def __init__(self, ):
        self.parts = []

    def add(self, part):
        self.parts.append(part)

    def show(self, ):
        print(self.parts)


class Builder():
    """
    Specify an abstract interface for creating parts of a Product object.
    """

    def __init__(self):
        self.story = Story()

    def _build_image(self):
        print("build image")

    def _build_music(self):
        print("build music")

    def _build_effet(self):
        print("build effet")

    def _build_video(self):
        print("build video")


class StoryDirector:
    """
Construct an object using the Builder interface.
"""

    def __init__(self):
        self._builder = None

    def construct(self, builder):
        self._builder = builder

    def basic_story(self, ):
        print("*** create basic story ***")
        self._builder._build_image()

    def photo_music_story(self, ):
        print("*** create photo + music story ***")
        self._builder._build_image()
        self._builder._build_music()
        self._builder._build_effet()

    def video_story(self, ):
        print("*** create video story ***")
        self._builder._build_video()
        self._builder._build_effet()

class FacebookConcreteBuilder(Builder):
    """
        Construct and assemble parts of the product by implementing the
        Builder interface.
        Define and keep track of the representation it creates.
        Provide an interface for retrieving the product.
    """
    def _build_image(self): self.story.add("image facebook")
    def _build_music(self): self.story.add("music facebook")
    def _build_effet(self): self.story.add("effect facebook")
    def _build_video(self): self.story.add("video facebook")

class InstagramConcreteBuilder(Builder):
    """
        Construct and assemble parts of the product by implementing the
        Builder interface.
        Define and keep track of the representation it creates.
        Provide an interface for retrieving the product.
    """
    def _build_image(self): self.story.add("image Instagram")
    def _build_music(self): self.story.add("music Instagram")
    def _build_effet(self): self.story.add("effect Instagram")
    def _build_video(self): self.story.add("video Instagram")

def main():
    concrete_builder = FacebookConcreteBuilder()
    director = StoryDirector()
    director.construct(concrete_builder)
    director.basic_story()
    story = concrete_builder.story
    story.show()
    concrete_builder2 = InstagramConcreteBuilder()
    director = StoryDirector()
    director.construct(concrete_builder2)
    director.video_story()
    story = concrete_builder2.story
    story.show()


if __name__ == "__main__":
    main()