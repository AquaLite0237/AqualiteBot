akinator.py
==========


Quick Examples
--------------

Here's a quick little example of the library being used to make a simple, text-based Akinator game:

.. code-block:: python

  import akinator

  aki = akinator.Akinator()

  q = aki.start_game()

  while aki.progression <= 80:
      a = input(q + "\n\t")
      if a == "b":
          try:
              q = aki.back()
          except akinator.CantGoBackAnyFurther:
              pass
      else:
          q = aki.answer(a)
  aki.win()

  correct = input(f"It's {aki.first_guess['name']} ({aki.first_guess['description']})! Was I correct?\n{aki.first_guess['absolute_picture_path']}\n\t")
  if correct.lower() == "yes" or correct.lower() == "y":
      print("Yay\n")
  else:
      print("Oof\n")

Here's the same game as above, but using the async version of the library instead:

.. code-block:: python

  from akinator.async_aki import Akinator
  import akinator
  import asyncio

  aki = Akinator()

  async def main():
      q = await aki.start_game()

      while aki.progression <= 80:
          a = input(q + "\n\t")
          if a == "b":
              try:
                  q = await aki.back()
              except akinator.CantGoBackAnyFurther:
                  pass
          else:
              q = await aki.answer(a)
      await aki.win()

      correct = input(f"It's {aki.first_guess['name']} ({aki.first_guess['description']})! Was I correct?\n{aki.first_guess['absolute_picture_path']}\n\t")
      if correct.lower() == "yes" or correct.lower() == "y":
          print("Yay\n")
      else:
          print("Oof\n")
      await aki.close()

  loop = asyncio.get_event_loop()
  loop.run_until_complete(main())
  loop.close()


Documentation
-------------

The async version of this library works almost exactly the same as the regular, non-async one. For the most part, both have the same classes, names of functions, etc. Any differences will be noted.

**Version Information**::

  >>> import akinator
  >>> akinator.__version__


*class* ``Akinator()``

A class that represents an Akinator game.

The first thing you want to do after creating an instance of this class is to call ``Akinator.start_game()``.

To get the **regular** Akinator class, make sure you've put ``import akinator`` at the top of your code. From there you can easily access the class via ``akinator.Akinator()``.

To get the **async** version of the class, make sure you have ``import akinator.async_aki`` or ``from akinator.async_aki import Akinator`` in your code and you'll be able to get the async Akinator class just as easily (Refer to the code examples above).


Functions
---------

.. note::

    In the async version, all the below functions are coroutines and must be awaited

start_game(*language=None, child_mode=False*)
  Start an Akinator game. Run this function first before the others. Returns a string containing the first question

  The ``language`` parameter can be left as None for English, the default language, or it can be set to one of the following (case-insensitive):

  - ``en``: English (default)
  - ``en_animals``: English server for guessing animals. Here, Akinator will attempt to guess the animal you're thinking instead of a character
  - ``en_objects``: English server for guessing objects. Here, Akinator will attempt to guess the object you're thinking instead of a character
  - ``ar``: Arabic
  - ``cn``: Chinese
  - ``de``: German
  - ``de_animals``: German server for guessing animals
  - ``es``: Spanish
  - ``es_animals``: Spanish server for guessing animals
  - ``fr``: French
  - ``fr_animals``: French server for guessing animals
  - ``fr_objects``: French server for guessing objects
  - ``il``: Hebrew
  - ``it``: Italian
  - ``it_animals``: Italian server for guessing animals
  - ``jp``: Japanese
  - ``jp_animals``: Japanese server for guessing animals
  - ``kr``: Korean
  - ``nl``: Dutch
  - ``pl``: Polish
  - ``pt``: Portuguese
  - ``ru``: Russian
  - ``tr``: Turkish
  - ``id``: Indonesian

  You can also put the name of the language spelled out, like ``spanish``, ``korean``, ``french_animals``, etc. If you put something else entirely, then then the ``InvalidLanguageError`` exception will be raised

  The ``child_mode`` parameter is False by default. If it's set to True, then Akinator won't ask questions about things that are NSFW

  **Important Note**: In the async version of the class, there's a third parameter: ``client_session`` (None by default). Here you can optionally specify an aiohttp ClientSession for the class functions to use when making API requests. If unspecified, a new ClientSession will be created

answer(*ans*)
  Answer the current question, which you can find with ``Akinator.question``. Returns a string containing the next question

  The ``ans`` parameter must be one of these (case-insensitive):

  - ``yes`` or ``y`` or ``0`` for YES
  - ``no`` or ``n`` or ``1`` for NO
  - ``i`` or ``idk`` or ``i dont know`` or ``i don't know`` or ``2`` for I DON'T KNOW
  - ``probably`` or ``p`` or ``3`` for PROBABLY
  - ``probably not`` or ``pn`` or ``4`` for PROBABLY NOT

  If it's something else, then the ``InvalidAnswerError`` exception will be raised

back()
  Goes back to the previous question. Returns a string containing that question

  If you're on the first question and you try to go back, the ``CantGoBackAnyFurther`` exception will be raised

win()
  Get Aki's guesses for who the person you're thinking of is based on your answers to the questions so far

  This function defines and returns the variable ``Akinator.first_guess``, a dictionary describing his first choice for who you're thinking about. The three most important values in the dict are ``name`` (character's name), ``description`` (description of character), and ``absolute_picture_path`` (direct link to image of character)
  Here's an example of what the dict looks like:

  .. code-block:: javascript

    {'absolute_picture_path': 'https://photos.clarinea.fr/BL_25_en/600/partenaire/c/2367495__1106501382.png',
     'award_id': '-1',
     'corrupt': '0',
     'description': 'Entrepreneur',
     'flag_photo': 0,
     'id': '49291',
     'id_base': '2367495',
     'name': 'Elon Musk',
     'picture_path': 'partenaire/c/2367495__1106501382.png',
     'proba': '0.925177',
     'pseudo': 'Elon Musk',
     'ranking': '229',
     'relative': '0',
     'valide_contrainte': '1'}

  This function also defines ``Akinator.guesses``, which is a list of dictionaries containing his choices in order from most likely to least likely

  It's recommended that you call this function when Aki's progression is above 80%. You can get his current progression via ``Akinator.progression``

close()
  **This function is only in the async version of the class**

  Close the aiohttp ClientSession. Call this function after the Akinator game is finished

  However, if you specified your own ClientSession in "Akinator.start_game()", you might actually not want to call this function


Variables
---------

These variables contain important information about the Akinator game. Please don't change any of these values in your program. It'll definitely break things.

uri
  The uri this Akinator game is using. Depends on what you put for the language param in ``Akinator.start_game()`` (e.g., ``"en.akinator.com"``, ``"fr.akinator.com"``, etc.)

server
  The server this Akinator game is using. Depends on what you put for the language param in ``Akinator.start_game()`` (e.g., ``"https://srv2.akinator.com:9162"``, ``"https://srv6.akinator.com:9127"``, etc.)

session
  A number, usually in between 0 and 100, that represents the game's session

signature
  A usually 9 or 10 digit number that represents the game's signature

uid
  The game's UID (unique identifier) for authentication purposes

frontaddr
  An IP address encoded in Base64; also for authentication purposes

child_mode
  A boolean that matches the child_mode param in ``Akinator.start_game()``

timestamp
  A POSIX timestamp for when ``Akinator.start_game()`` was called

question
  The current question that Akinator is asking the user. Examples of questions asked by Aki include: ``Is your character's gender female?``, ``Is your character more than 40 years old?``, ``Does your character create music?``, ``Is your character real?``, ``Is your character from a TV series?``, etc.

progression
  A floating point number that represents a percentage showing how close Aki thinks he is to guessing your character. I recommend keeping track of this value and calling ``Akinator.win()`` when it's above 80 or 90. In most cases, this is about when Aki will have it narrowed down to one choice, which will hopefully be the correct one

step
  An integer that tells you what question Akinator is on. This will be 0 on the first question, 1 on the second question, 2 on the third, 3 on the fourth, etc.

first_guess
  A dict that describes Akinator's first guess for who your character is. An example of what this dict will look like can be found in the documentation for the ``Akinator.win()`` function above. This variable will only be defined once that function is called

guesses
  A list of dicts containing his choices in order from most likely to least likely. Each dict will look the same as ``first_guess``. This list will also contain ``first_guess`` as the first entry. This variable will only be defined once ``Akinator.win()`` is called

client_session
  An aiohttp ClientSession object that is used when making API requests. This variable is only present in the async version of the class

The first 8 variables—``uri``, ``server``, ``session``, ``signature``, ``uid``, ``frontaddr``, ``child_mode``, and ``timestamp``—will remain unchanged, but the next 3—``question``, ``progression``, and ``step``—will change as you go on. The final two—``first_guess`` and ``guesses``— will only be defined when ``Akinator.win()`` is called.

``client_session``, which is only in the async version of the class, will not change once it's been set, but calling ``Akinator.close()`` will reset it to None.


Exceptions
----------

Exceptions that are thrown by the library

InvalidAnswerError
  Raised when the user inputs an invalid answer into ``Akinator.answer()``. Subclassed from ``ValueError``

InvalidLanguageError
  Raised when the user inputs an invalid language into ``Akinator.start_game()``. Subclassed from ``ValueError``

AkiConnectionFailure
  Raised if the Akinator API fails to connect for some reason. Base class for ``AkiTimedOut``, ``AkiNoQuestions``, ``AkiServerDown``, and ``AkiTechnicalError``

AkiTimedOut
  Raised if the Akinator session times out. Derived from ``AkiConnectionFailure``

AkiNoQuestions
  Raised if the Akinator API runs out of questions to ask. This will happen if ``Akinator.step`` is at 79 and the ``answer`` function is called again. Derived from ``AkiConnectionFailure``

AkiServerDown
  Raised if Akinator's servers are down for the region you're running on. If this happens, try again later or use a different language. Derived from ``AkiConnectionFailure``

AkiTechnicalError
  Raised if Aki's servers had a technical error. If this happens, try again later or use a different language. Derived from ``AkiConnectionFailure``

CantGoBackAnyFurther:
  Raised when the user is on the first question and tries to go back further by calling ``Akinator.back()``
