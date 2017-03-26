class Literature:
    def __init__(self, author, title, poem_list, syntax):
        self.author = author
        self.title = title
        self.poem_list = poem_list
        self.syntax = syntax
        self.header = ""

    def retrieve(self, stanza):
        if stanza in range(1, len(self.poem_list) + 1):
            self.header = """```python
AUTHOR: "%s" | TITLE: "%s [Stanza %s]```""" % (self.author, self.title, str(stanza))
            self.stanza_text = self.poem_list[stanza - 1]

            self.poem_object = {
                "header": self.header,
                "text": self.stanza_text
            }

            return self.poem_object


the_raven = [
    """
    ```Once upon a midnight dreary, while I pondered, weak and weary,
    Over many a quaint and curious volume of forgotten lore—
        While I nodded, nearly napping, suddenly there came a tapping,
    As of some one gently rapping, rapping at my chamber door.
    “’Tis some visitor,” I muttered, “tapping at my chamber door—
                Only this and nothing more.”```""",

    """
    ```Ah, distinctly I remember it was in the bleak December;
    And each separate dying ember wrought its ghost upon the floor.
        Eagerly I wished the morrow;—vainly I had sought to borrow
        From my books surcease of sorrow—sorrow for the lost Lenore—
    For the rare and radiant maiden whom the angels name Lenore—
                Nameless here for evermore.```""",

    """
    ```And the silken, sad, uncertain rustling of each purple curtain
    Thrilled me—filled me with fantastic terrors never felt before;
        So that now, to still the beating of my heart, I stood repeating
        “’Tis some visitor entreating entrance at my chamber door—
    Some late visitor entreating entrance at my chamber door;—
                This it is and nothing more.”```""",

    """
    ```Presently my soul grew stronger; hesitating then no longer,
    “Sir,” said I, “or Madam, truly your forgiveness I implore;
        But the fact is I was napping, and so gently you came rapping,
        And so faintly you came tapping, tapping at my chamber door,
    That I scarce was sure I heard you”—here I opened wide the door;—
                Darkness there and nothing more.```""",

    """
    ```Deep into that darkness peering, long I stood there wondering, fearing,
    Doubting, dreaming dreams no mortal ever dared to dream before;
        But the silence was unbroken, and the stillness gave no token,
        And the only word there spoken was the whispered word, “Lenore?”
    This I whispered, and an echo murmured back the word, “Lenore!”—
                Merely this and nothing more.```""",

    """
    ```Back into the chamber turning, all my soul within me burning,
    Soon again I heard a tapping somewhat louder than before.
        “Surely,” said I, “surely that is something at my window lattice;
          Let me see, then, what thereat is, and this mystery explore—
    Let my heart be still a moment and this mystery explore;—
                ’Tis the wind and nothing more!”```""",

    """
    ```Open here I flung the shutter, when, with many a flirt and flutter,
    In there stepped a stately Raven of the saintly days of yore;
        Not the least obeisance made he; not a minute stopped or stayed he;
        But, with mien of lord or lady, perched above my chamber door—
    Perched upon a bust of Pallas just above my chamber door—
                Perched, and sat, and nothing more.```""",

    """
    ```Then this ebony bird beguiling my sad fancy into smiling,
    By the grave and stern decorum of the countenance it wore,
    “Though thy crest be shorn and shaven, thou,” I said, “art sure no craven,
    Ghastly grim and ancient Raven wandering from the Nightly shore—
    Tell me what thy lordly name is on the Night’s Plutonian shore!”
                Quoth the Raven “Nevermore.”```""",

    """
    ```Much I marvelled this ungainly fowl to hear discourse so plainly,
    Though its answer little meaning—little relevancy bore;
        For we cannot help agreeing that no living human being
        Ever yet was blessed with seeing bird above his chamber door—
    Bird or beast upon the sculptured bust above his chamber door,
                With such name as “Nevermore.”```""",

    """
    ```But the Raven, sitting lonely on the placid bust, spoke only
    That one word, as if his soul in that one word he did outpour.
        Nothing farther then he uttered—not a feather then he fluttered—
        Till I scarcely more than muttered “Other friends have flown before—
    On the morrow he will leave me, as my Hopes have flown before.”
                Then the bird said “Nevermore.”```""",

    """
    ```Startled at the stillness broken by reply so aptly spoken,
    “Doubtless,” said I, “what it utters is its only stock and store
        Caught from some unhappy master whom unmerciful Disaster
        Followed fast and followed faster till his songs one burden bore—
    Till the dirges of his Hope that melancholy burden bore
                Of ‘Never—nevermore’.”```""",

    """
    ```But the Raven still beguiling all my fancy into smiling,
    Straight I wheeled a cushioned seat in front of bird, and bust and door;
        Then, upon the velvet sinking, I betook myself to linking
        Fancy unto fancy, thinking what this ominous bird of yore—
    What this grim, ungainly, ghastly, gaunt, and ominous bird of yore
                Meant in croaking “Nevermore.”```""",

    """
    ```This I sat engaged in guessing, but no syllable expressing
    To the fowl whose fiery eyes now burned into my bosom’s core;
        This and more I sat divining, with my head at ease reclining
        On the cushion’s velvet lining that the lamp-light gloated o’er,
    But whose velvet-violet lining with the lamp-light gloating o’er,
                She shall press, ah, nevermore!```""",

    """
    ```Then, methought, the air grew denser, perfumed from an unseen censer
    Swung by Seraphim whose foot-falls tinkled on the tufted floor.
        “Wretch,” I cried, “thy God hath lent thee—by these angels he hath sent thee
        Respite—respite and nepenthe from thy memories of Lenore;
    Quaff, oh quaff this kind nepenthe and forget this lost Lenore!”
                Quoth the Raven “Nevermore.”```""",

    """
    ```“Prophet!” said I, “thing of evil!—prophet still, if bird or devil!—
    Whether Tempter sent, or whether tempest tossed thee here ashore,
        Desolate yet all undaunted, on this desert land enchanted—
        On this home by Horror haunted—tell me truly, I implore—
    Is there—is there balm in Gilead?—tell me—tell me, I implore!”
                Quoth the Raven “Nevermore.”```""",

    """
    ```“Prophet!” said I, “thing of evil!—prophet still, if bird or devil!
    By that Heaven that bends above us—by that God we both adore—
        Tell this soul with sorrow laden if, within the distant Aidenn,
        It shall clasp a sainted maiden whom the angels name Lenore—
    Clasp a rare and radiant maiden whom the angels name Lenore.”
                Quoth the Raven “Nevermore.”```""",

    """
    ```“Be that word our sign of parting, bird or fiend!” I shrieked, upstarting—
    “Get thee back into the tempest and the Night’s Plutonian shore!
        Leave no black plume as a token of that lie thy soul hath spoken!
        Leave my loneliness unbroken!—quit the bust above my door!
    Take thy beak from out my heart, and take thy form from off my door!”
                Quoth the Raven “Nevermore.”```""",

    """
    ```And the Raven, never flitting, still is sitting, still is sitting
    On the pallid bust of Pallas just above my chamber door;
        And his eyes have all the seeming of a demon’s that is dreaming,
        And the lamp-light o’er him streaming throws his shadow on the floor;
    And my soul from out that shadow that lies floating on the floor
                Shall be lifted—nevermore!```"""]
do_not_weep = [
    """
    ```Do not stand at my grave and weep
    I am not there. I do not sleep.
    I am a thousand winds that blow.
    I am the diamond glints on snow.
    I am the sunlight on ripened grain.
    I am the gentle autumn rain.
    When you awaken in the morning's hush
    I am the swift uplifting rush
    Of quiet birds in circled flight.
    I am the soft stars that shine at night.
    Do not stand at my grave and cry;
    I am not there. I did not die.```"""]
for_annie = [
    """
    ```Thank Heaven! the crisis,
    The danger, is past,
    And the lingering illness
    Is over at last—
    And the fever called "Living"
    Is conquered at last.```""",

    """
    ```Sadly, I know
    I am shorn of my strength,
    And no muscle I move
    As I lie at full length—
    But no matter!—I feel
    I am better at length.```""",

    """
    ```And I rest so composedly,
    Now, in my bed,
    That any beholder
    Might fancy me dead—
    Might start at beholding me,
    Thinking me dead.```""",

    """
    ```The moaning and groaning,
    The sighing and sobbing,
    Are quieted now,
    With that horrible throbbing
    At heart:—ah, that horrible,
    Horrible throbbing!```""",

    """
    ```The sickness—the nausea—
    The pitiless pain—
    Have ceased, with the fever
    That maddened my brain—
    With the fever called "Living"
    That burned in my brain.```""",

    """
    ```And oh! of all tortures
    That torture the worst
    Has abated—the terrible
    Torture of thirst
    For the naphthaline river
    Of Passion accurst:—
    I have drank of a water
    That quenches all thirst:—```""",

    """
    ```Of a water that flows,
    With a lullaby sound,
    From a spring but a very few
    Feet under ground—
    From a cavern not very far
    Down under ground.```""",

    """
    ```And ah! let it never
    Be foolishly said
    That my room it is gloomy
    And narrow my bed;
    For man never slept
    In a different bed—
    And, to sleep, you must slumber
    In just such a bed.```""",

    """
    ```My tantalized spirit
    Here blandly reposes,
    Forgetting, or never
    Regretting, its roses—
    Its old agitations
    Of myrtles and roses:```""",

    """
    ```For now, while so quietly
    Lying, it fancies
    A holier odor
    About it, of pansies—
    A rosemary odor,
    Commingled with pansies—
    With rue and the beautiful
    Puritan pansies.```""",

    """
    ```And so it lies happily,
    Bathing in many
    A dream of the truth
    And the beauty of Annie—
    Drowned in a bath
    Of the tresses of Annie.```""",

    """
    ```She tenderly kissed me,
    She fondly caressed,
    And then I fell gently
    To sleep on her breast—
    Deeply to sleep
    From the heaven of her breast.```""",

    """
    ```When the light was extinguished,
    She covered me warm,
    And she prayed to the angels
    To keep me from harm—
    To the queen of the angels
    To shield me from harm.```""",

    """
    ```And I lie so composedly,
    Now, in my bed,
    (Knowing her love)
    That you fancy me dead—
    And I rest so contentedly,
    Now in my bed
    (With her love at my breast).
    That you fancy me dead—
    That you shudder to look at me,
    Thinking me dead:—```""",

    """
    ```But my heart it is brighter
    Than all of the many
    Stars in the sky,
    For it sparkles with Annie—
    It glows with the light
    Of the love of my Annie—
    With the thought of the light
    Of the eyes of my Annie.```"""]
alone = [
    """
    ```From childhood’s hour I have not been
    As others were—I have not seen
    As others saw—I could not bring
    My passions from a common spring—
    From the same source I have not taken
    My sorrow—I could not awaken
    My heart to joy at the same tone—
    And all I lov’d—I lov’d alone—
    Then—in my childhood—in the dawn
    Of a most stormy life—was drawn
    From ev’ry depth of good and ill
    The mystery which binds me still—
    From the torrent, or the fountain—
    From the red cliff of the mountain—
    From the sun that ’round me roll’d
    In its autumn tint of gold—
    From the lightning in the sky
    As it pass’d me flying by—
    From the thunder, and the storm—
    And the cloud that took the form
    (When the rest of Heaven was blue)
    Of a demon in my view—```"""
]
annabel_lee = [
    """
    ```It was many and many a year ago,
       In a kingdom by the sea,
    That a maiden there lived whom you may know
       By the name of Annabel Lee;
    And this maiden she lived with no other thought
       Than to love and be loved by me.```""",

    """
    ```I was a child and she was a child,
       In this kingdom by the sea,
    But we loved with a love that was more than love—
       I and my Annabel Lee—
    With a love that the wingèd seraphs of Heaven
       Coveted her and me.```""",

    """
    ```And this was the reason that, long ago,
       In this kingdom by the sea,
    A wind blew out of a cloud, chilling
       My beautiful Annabel Lee;
    So that her highborn kinsmen came
       And bore her away from me,
    To shut her up in a sepulchre
       In this kingdom by the sea.```""",

    """
    ```The angels, not half so happy in Heaven,
       Went envying her and me—
    Yes!—that was the reason (as all men know,
       In this kingdom by the sea)
    That the wind came out of the cloud by night,
       Chilling and killing my Annabel Lee.```""",

    """
    ```But our love it was stronger by far than the love
       Of those who were older than we—
       Of many far wiser than we—
    And neither the angels in Heaven above
       Nor the demons down under the sea
    Can ever dissever my soul from the soul
       Of the beautiful Annabel Lee;```""",

    """
    ```For the moon never beams, without bringing me dreams
       Of the beautiful Annabel Lee;
    And the stars never rise, but I feel the bright eyes
       Of the beautiful Annabel Lee;
    And so, all the night-tide, I lie down by the side
       Of my darling—my darling—my life and my bride,
       In her sepulchre there by the sea—
       In her tomb by the sounding sea.```"""]
one_art = [
    """
    ```The art of losing isn’t hard to master;
    so many things seem filled with the intent
    to be lost that their loss is no disaster.```""",

    """
    ```Lose something every day. Accept the fluster
    of lost door keys, the hour badly spent.
    The art of losing isn’t hard to master.```""",

    """
    ```Then practice losing farther, losing faster:
    places, and names, and where it was you meant
    to travel. None of these will bring disaster.```""",

    """
    ```I lost my mother’s watch. And look! my last, or
    next-to-last, of three loved houses went.
    The art of losing isn’t hard to master.```""",

    """
    ```I lost two cities, lovely ones. And, vaster,
    some realms I owned, two rivers, a continent.
    I miss them, but it wasn’t a disaster.```""",

    """
    ```—Even losing you (the joking voice, a gesture
    I love) I shan’t have lied. It’s evident
    the art of losing’s not too hard to master
    though it may look like (Write it!) like disaster.```"""]
much_madness = [
    """
    ```Much Madness is divinest Sense -
    To a discerning Eye -
    Much Sense - the starkest Madness -
    ’Tis the Majority
    In this, as all, prevail -
    Assent - and you are sane -
    Demur - you’re straightway dangerous -
    And handled with a Chain -```"""]
light_brigade = [
    """
    ```Half a league, half a league,
    Half a league onward,
    All in the valley of Death
       Rode the six hundred.
    “Forward, the Light Brigade!
    Charge for the guns!” he said.
    Into the valley of Death
       Rode the six hundred.```""",

    """
    ```"“Forward, the Light Brigade!”
    Was there a man dismayed?
    Not though the soldier knew
       Someone had blundered.
       Theirs not to make reply,
       Theirs not to reason why,
       Theirs but to do and die.
       Into the valley of Death
       Rode the six hundred.```""",

    """
    ```Cannon to right of them,
    Cannon to left of them,
    Cannon in front of them
       Volleyed and thundered;
    Stormed at with shot and shell,
    Boldly they rode and well,
    Into the jaws of Death,
    Into the mouth of hell
       Rode the six hundred.```""",

    """
    ```Flashed all their sabres bare,
    Flashed as they turned in air
    Sabring the gunners there,
    Charging an army, while
       All the world wondered.
    Plunged in the battery-smoke
    Right through the line they broke;
    Cossack and Russian
    Reeled from the sabre stroke
       Shattered and sundered.
    Then they rode back, but not
       Not the six hundred.```""",

    """
    ```Cannon to right of them,
    Cannon to left of them,
    Cannon behind them
       Volleyed and thundered;
    Stormed at with shot and shell,
    While horse and hero fell.
    They that had fought so well
    Came through the jaws of Death,
    Back from the mouth of hell,
    All that was left of them,
       Left of six hundred.```""",

    """
    ```When can their glory fade?
    O the wild charge they made!
       All the world wondered.
    Honour the charge they made!
    Honour the Light Brigade,
       Noble six hundred!```"""]
the_tyger = [
    """
    ```Tyger Tyger, burning bright,
    In the forests of the night;
    What immortal hand or eye,
    Could frame thy fearful symmetry?```""",

    """
    ```In what distant deeps or skies.
    Burnt the fire of thine eyes?
    On what wings dare he aspire?
    What the hand, dare seize the fire?```""",

    """
    ```And what shoulder, & what art,
    Could twist the sinews of thy heart?
    And when thy heart began to beat,
    What dread hand? & what dread feet?```""",

    """
    ```What the hammer? what the chain,
    In what furnace was thy brain?
    What the anvil? what dread grasp,
    Dare its deadly terrors clasp!```""",

    """
    ```When the stars threw down their spears
    And water'd heaven with their tears:
    Did he smile his work to see?
    Did he who made the Lamb make thee?```""",

    """
    ```Tyger Tyger burning bright,
    In the forests of the night:
    What immortal hand or eye,
    Dare frame thy fearful symmetry?```"""]
stopping_by_woods = [
    """
    ```Whose woods these are I think I know.
    His house is in the village though;
    He will not see me stopping here
    To watch his woods fill up with snow.```""",

    """
    ```My little horse must think it queer
    To stop without a farmhouse near
    Between the woods and frozen lake
    The darkest evening of the year.```""",

    """
    ```He gives his harness bells a shake
    To ask if there is some mistake.
    The only other sound’s the sweep
    Of easy wind and downy flake.```""",

    """
    ```The woods are lovely, dark and deep,
    But I have promises to keep,
    And miles to go before I sleep,
    And miles to go before I sleep.```"""]
desiderata = [
    """
    ```Go placidly amid the noise and haste,
    and remember what peace there may be in silence.
    As far as possible without surrender
    be on good terms with all persons.
    Speak your truth quietly and clearly;
    and listen to others,
    even the dull and the ignorant;
    they too have their story.```""",

    """
    ```Avoid loud and aggressive persons,
    they are vexations to the spirit.
    If you compare yourself with others,
    you may become vain and bitter;
    for always there will be greater and lesser persons than yourself.
    Enjoy your achievements as well as your plans.```""",

    """
    ```Keep interested in your own career, however humble;
    it is a real possession in the changing fortunes of time.
    Exercise caution in your business affairs;
    for the world is full of trickery.
    But let this not blind you to what virtue there is;
    many persons strive for high ideals;
    and everywhere life is full of heroism.```""",

    """
    ```Be yourself.
    Especially, do not feign affection.
    Neither be cynical about love;
    for in the face of all aridity and disenchantment
    it is as perennial as the grass.```""",

    """
    ```Take kindly the counsel of the years,
    gracefully surrendering the things of youth.
    Nurture strength of spirit to shield you in sudden misfortune.
    But do not distress yourself with dark imaginings.
    Many fears are born of fatigue and loneliness.
    Beyond a wholesome discipline,
    be gentle with yourself.```""",

    """
    ```You are a child of the universe,
    no less than the trees and the stars;
    you have a right to be here.
    And whether or not it is clear to you,
    no doubt the universe is unfolding as it should.```""",

    """
    ```Therefore be at peace with God,
    whatever you conceive Him to be,
    and whatever your labors and aspirations,
    in the noisy confusion of life keep peace with your soul.```""",

    """
    ```With all its sham, drudgery, and broken dreams,
    it is still a beautiful world.
    Be cheerful.
    Strive to be happy.```"""]
first_they_came = [
    """
    ```First they came for the Socialists, and I did not speak out—
    Because I was not a Socialist.```""",

    """
    ```Then they came for the Trade Unionists, and I did not speak out—
    Because I was not a Trade Unionist.```""",

    """
    ```Then they came for the Jews, and I did not speak out—
    Because I was not a Jew.```""",

    """```Then they came for me—and there was no one left to speak for me.```"""]
kandari_hushiar = [
    """
    ```Impregnable mountains, horizonless desert
    Murky fathomless ocean O
    Crossing in the nights darkness
    Travelers: At once take note!```""",

    """
    ```The boat trembles, the water swells
    The boatmans without a way
    The sails in tatters, somebody to catch the rudder
    Who has the courage, ho?
    Are you that youth? Hurry forth!
    You, the future beckons
    Heavy is the storm, crossing it is the cause
    The boat must land at the distant shore!```""",

    """
    ```Peerless the darkness haunts
    On guard! Leaders of the Motherland and soldiers, too!
    Ancient grievances have raised their heads
    The deprived souls heave with passion
    To achieve a fair hearing
    They, too, must come along!```""",

    """
    ```The hapless nation drowns, for swim it cannot
    O Captain! Today you shall be watched
    For determination and love
    Hindu or Muslim? Wait! Who asks?
    Captain! Proclaim: My Mother's children are drowning Human all!```""",

    """
    ```Perils abound the mountains; fear, the travelers, assails
    Thunder sonorous rumbles
    Turning back strikes as unsound
    Captain! Forget not your way; abandon not your post
    Through strife, heave ho
    You've assumed a duty profound!```""",

    """
    ```Captain! The fields of Palashi recall
    With the blood of the Bangali Clive bloodied his sword
    Into the Ganga plunged India's sun, snuffed out
    That sun will rise yet again, blood red in our blood!```""",

    """
    ```Those who sang away their lives on the hangman's gallows
    At watch, they softly surround; your sacrifice, what shall it be?
    While the nation stands tested, just one's race appease?
    The boat trembles, the water swells, Captain: Beware!```"""]
max_und_moritz = [
    """
    ```Max und Moritz machten beide,
    Als sie lebten, keinem Freude:
    Bildlich siehst du jetzt die Possen,
    Die in Wirklichkeit verdrossen,
    Mit behaglichem Gekicher,
    Weil du selbst vor ihnen sicher.
    Aber das bedenke stets:
    Wie man's treibt, mein Kind, so geht's.```""",

    """
    ```Ach, was muß man oft von bösen
    Kindern hören oder lesen!
    Wie zum Beispiel hier von diesen,
    Welche Max und Moritz hießen;
    Die, anstatt durch weise Lehren
    Sich zum Guten zu bekehren,
    Oftmals noch darüber lachten
    Und sich heimlich lustig machten.
    Ja, zur Übeltätigkeit,
    Ja, dazu ist man bereit!
    Menschen necken, Tiere quälen,
    Äpfel, Birnen, Zwetschgen stehlen,
    Das ist freilich angenehmer
    Und dazu auch viel bequemer,
    Als in Kirche oder Schule
    Festzusitzen auf dem Stuhle.
    Aber wehe, wehe, wehe!
    Wenn ich auf das Ende sehe!!
    Ach, das war ein schlimmes Ding,
    Wie es Max und Moritz ging!
    Drum ist hier, was sie getrieben,
    Abgemalt und aufgeschrieben.```""",

    """
    ```Mancher gibt sich viele Müh'
    Mit dem lieben Federvieh;
    Einesteils der Eier wegen,
    Welche diese Vögel legen;
    Zweitens: Weil man dann und wann
    Einen Braten essen kann;
    Drittens aber nimmt man auch
    Ihre Federn zum Gebrauch
    In die Kissen und die Pfühle,
    Denn man liegt nicht gerne kühle.
    Seht, da ist die Witwe Bolte,
    Die das auch nicht gerne wollte.```""",

    """
    ```Ihrer Hühner waren drei
    Und ein stolzer Hahn dabei.
    Max und Moritz dachten nun:
    Was ist hier jetzt wohl zu tun?
    Ganz geschwinde, eins, zwei, drei,
    Schneiden sie sich Brot entzwei,
    In vier Teile, jedes Stück
    Wie ein kleiner Finger dick.
    Diese binden sie an Fäden,
    Übers Kreuz, ein Stück an jeden,
    Und verlegen sie, genau
    In den Hof der guten Frau.
    Kaum hat dies der Hahn gesehen,
    Fängt er auch schon an zu krähen:
    Kikeriki! Kikikerikih!! -
    Tak, tak, tak! - Da kommen sie.
    Hahn und Hühner schlucken munter
    jedes ein Stück Brot hinunter;
    Aber als sie sich besinnen,
    Konnte keines recht von hinnen.
    In die Kreuz und in die Quer
    Reißen sie sich hin und her,
    Flattern auf und in die Höh',
    Ach herrje, herrjemine!
    Ach, sie bleiben an dem langen,
    Dürren Ast des Baumes hangen.```""",

    """
    ```Und ihr Hals wird lang und länger,
    Ihr Gesang wird bang und bänger.
    jedes legt noch schnell ein Ei,
    Und dann kommt der Tod herbei.
    Witwe Bolte in der Kammer
    Hört im Bette diesen Jammer;
    Ahnungsvoll tritt sie heraus,
    Ach, was war das für ein Graus!
    ",Fließet aus dem Aug', ihr Tränen!
    All mein Hoffen, all mein Sehnen,
    Meines Lebens schönster Traum
    Hängt an diesem Apfelbaum!'
    Tiefbetrübt und sorgenschwer
    Kriegt sie jetzt das Messer her,
    Nimmt die Toten von den Strängen,
    Dass sie so nicht länger hängen,
    Und mit stummem Trauerblick
    Kehrt sie in ihr Haus zurück.
    Dieses war der erste Streich,
    Doch der zweite folgt sogleich.```""",

    """
    ```Als die gute Witwe Bolte
    Sich von ihrem Schmerz erholte,
    Dachte sie so hin und her,
    Dass es wohl das beste wär',
    Die Verstorbnen, die hienieden
    Schon so frühe abgeschieden,
    Ganz im stillen und in Ehren
    Gut gebraten zu verzehren.
    Freilich war die Trauer groß,
    Als sie nun so nackt und bloß
    Abgerupft am Herde lagen,
    Sie, die einst in schönen Tagen
    Bald im Hofe, bald im Garten
    Lebensfroh im Sande scharrten. -
    Ach, Frau Bolte weint aufs neu,
    Und der Spitz steht auch dabei.
    Max und Moritz rochen dieses.
    ..Schnell aufs Dach gekrochen!' hieß es.
    Durch den Schornstein mit Vergnügen
    Sehen sie die Hühner liegen,
    Die schon ohne Kopf und Gurgeln
    Lieblich in der Pfanne schmurgeln.
    Eben geht mit einem Teller
    Witwe Bolte in den Keller,
    Dass sie von dem Sauerkohle
    Eine Portion sich hole,
    Wofür sie besonders schwärmt,
    Wenn er wieder aufgewärmt.
    Unterdessen auf dem Dache
    Ist man tätig bei der Sache.```""",

    """
    ```Max hat schon mit Vorbedacht
    Eine Angel mitgebracht.
    Schnupdiwup! Da wird nach oben
    Schon ein Huhn heraufgehoben.
    Schnupdiwup! jetzt Numro zwei;
    Schnupdiwup! jetzt Numro drei;
    Und jetzt kommt noch Numro vier:
    Schnupdiwup! Dich haben wir!
    Zwar der Spitz sah es genau,
    Und er bellt: Rawau! Rawau!
    Aber schon sind sie ganz munter
    Fort und von dem Dach herunter.
    Na! Das wird Spektakel geben,
    Denn Frau Bolte kommt soeben;
    Angewurzelt stand sie da,
    Als sie nach der Pfanne sah.
    Alle Hühner waren fort. -
    "Spitz!!" - Das war ihr erstes Wort.
    "O du Spitz, du Ungetüm!
    Aber wart! Ich komme ihm!-
    Mit dem Löffel groß und schwer
    geht es über Spitzen her;
    Laut ertönt sein Wehgeschrei
    Denn er fühlt sich schuldenfrei.
    Max und Moritz im Verstecke
    Schnarchen aber an der Hecke
    Und vom ganzen Hühnerschmaus
    Guckt nur noch ein Bein heraus.
    Dieses war der zweite Streich,
    Doch der dritte folgt sogleich.```""",

    """
    ```Jedermann im Dorfe kannte
    Einen, der sich Böck benannte.
    Alltagsröcke, Sonntagsröcke,
    Lange Hosen, spitze Fräcke,
    Westen mit bequemen Taschen,
    Warme Mäntel und Gamaschen,
    Alle diese Kleidungssachen
    Wusste Schneider Bock zu machen.
    Oder wäre was zu flicken,
    Abzuschneiden, anzustücken,
    Oder gar ein Knopf der Hose
    Abgerissen oder lose,
    Wie und wo und wann es sei,
    Hinten, vorne, einerlei,
    Alles macht der Meister Böck,
    Denn das ist sein Lebenszweck.
    Drum so hat in der Gemeinde
    Jedermann ihn gern zum Freunde.
    Aber Max und Moritz dachten,
    Wie sie ihn verdrießlich machten.
    Nämlich vor des Meisters Hause
    Floß ein Wasser mit Gebrause.
    Übers Wasser führt ein Steg,
    Und darüber geht der Weg.
    Max und Moritz, gar nicht träge,
    Sägen heimlich mit der Säge,
    Ritzeratze! voller Tücke,
    In die Brücke eine, Lücke.
    Als nun diese Tat vorbei,
    Hört man plötzlich ein Geschrei:
    "He, heraus! Du Ziegen-Böck!
    Schneider, Schneider, meck, meck, meck!"```""",

    """
    ```Alles konnte Böck ertragen,
    Ohne nur ein Wort zu sagen;
    Aber wenn er dies erfuhr,
    Ging's ihm wider die Natur.
    Schnelle springt er mit der Elle
    Ober seines Hauses Schwelle,
    Denn schon wieder ihm zum Schreck
    Tönt ein lautes: "Meck, meck, meck!"
    Und schon ist er auf der Brücke,
    Kracks! Die Brücke bricht in Stücke;
    Wieder tönt es: Meck, meck, meck!
    Plumps! Da ist der Schneider weg!
    Grad als dieses vorgekommen,
    Kommt ein Gänsepaar geschwommen,
    Welches Böck in Todeshast
    Krampfhaft bei den Beinen fasst.
    Beide Gänse in der Hand,
    Flattert er auf trocknes Land.
    Übrigens bei alledem
    Ist so etwas nicht bequem;
    Wie denn Böck von der Geschichte
    Auch das Magendrücken kriegte.
    Hoch ist hier Frau Böck zu preisen!
    Denn ein heißes Bügeleisen,
    Auf den kalten Leib gebracht,
    Hat es wiedergutgemacht.
    Bald im Dorf hinauf, hinunter,
    Hieß es: Böck ist wieder munter!'
    Dieses war der dritte Streich,
    Doch der vierte folgt sogleich.```""",

    """
    ```Also lautet ein Beschluß,
    Daß der Mensch was lernen muß.
    Nicht allein das Abc
    Bringt den Menschen in die Höh';
    Nicht allein in Schreiben, Lesen
    Übt sich ein vernünftig Wesen;
    Nicht allein in Rechnungssachen
    Soll der Mensch sich Mühe machen,
    Sondern auch der Weisheit Lehren
    Muss man mit Vergnügen hören.
    Dass dies mit Verstand geschah,
    War Herr Lehrer Lämpel da.
    Max und Moritz, diese beiden,
    Mochten ihn darum nicht leiden;
    Denn wer böse Streiche macht,
    Gibt nicht auf den Lehrer acht.
    Nun war dieser brave Lehrer
    Von dem Tobak ein Verehrer,
    Was man ohne alle Frage
    Nach des Tages Müh und Plage
    Einem guten, alten Mann
    Auch von Herzen gönnen kann.
    Max und Moritz, unverdrossen,
    Sinnen aber schon auf Possen,
    Ob vermittelst seiner Pfeifen
    Dieser Mann nicht anzugreifen.
    Einstens, als es Sonntag wieder
    Und Herr Lämpel, brav und bieder,
    In der Kirche mit Gefühle
    Saß vor seinem Orgelspiele,
    Schlichen sich die bösen Buben
    In sein Haus und seine Stuben
    Wo die Meerschaumpfeife stand;
    Max hält sie in seiner Hand;
    Aber Moritz aus der Tasche
    Zieht die Flintenpulverflasche,
    Und geschwinde, stopf, stopf, stopf!
    Pulver in den Pfeifenkopf. -```""",

    """
    ```jetzt nur still und schnell nach Haus,
    Denn schon ist die Kirche aus. -
    Eben schließt in sanfter Ruh
    Lämpel seine Kirche zu;
    Und mit Buch und Notenheften
    Nach besorgten Amtsgeschäften
    Lenkt er freudig seine Schritte
    Zu der heimatlichen Hütte,
    Und voll Dankbarkeit sodann
    Zündet er sein Pfeifchen an.
    "Ach!" - spricht er - Die größte Freud
    Ist doch die Zufriedenheit!!"
    Rums!! - Da geht die Pfeife los
    Mit Getöse, schrecklich groß.
    Kaffeetopf und Wasserglas,
    Tobaksdose, Tintenfass,
    Ofen, Tisch und Sorgensitz
    Alles fliegt im Pulverblitz.
    Als der Dampf sich nun erhob,
    Sieht man Lämpel, der gottlob
    Lebend auf dem Rücken liegt;
    Doch er hat was abgekriegt.
    Nase, Hand, Gesicht und Ohren
    Sind so schwarz als wie die Mohren,
    Und des Haares letzter Schopf
    Ist verbrannt bis auf den Kopf.
    Wer soll nun die Kinder lehren
    Und die Wissenschaft vermehren?
    Wer soll nun für Lämpel leiten
    Seine Amtestätigkeiten?
    Woraus soll der Lehrer rauchen,
    Wenn die Pfeife nicht zu brauchen?
    Mit der Zeit wird alles heil,
    Nur die Pfeife hat ihr Teil.
    Dieses war der vierte Streich,
    Doch der fünfte folgt sogleich.```""",

    """
    ```Wer in Dorfe oder Stadt
    Einen Onkel wohnen hat,
    Der sei höflich und bescheiden,
    Denn das mag der Onkel leiden.
    Morgens sagt man: "Guten Morgen!
    Haben Sie was zu besorgen?"
    Bringt ihm, was er haben muss:
    Zeitung, Pfeife, Fidibus.
    Oder sollt' es wo im Rücken
    Drücken, beißen oder zwicken,
    Gleich ist man mit Freudigkeit
    Dienstbeflissen und bereit.
    Oder sei's nach einer Prise,
    Dass der Onkel heftig niese,
    Ruft man: "Prosit!" also gleich.
    "Danke!" - "Wohl bekomm' es Euch!"
    Oder kommt er spät nach Haus,
    Zieht man ihm die Stiefel aus,
    Holt Pantoffel, Schlafrock, Mütze,
    Daß er nicht im Kalten sitze -
    Kurz, man ist darauf 'bedacht,
    Was dem Onkel Freude macht.
    Max und Moritz ihrerseits
    Fanden darin keinen Reiz.
    Denkt euch nur, welch schlechten Witz
    Machten sie mit Onkel Fritz!
    jeder weiß, was so ein Mai=
    Käfer für ein Vogel sei.
    In den Bäumen hin und her
    Fliegt und kriecht und krabbelt er.```""",

    """
    ```Max und Moritz, immer munter,
    Schütteln sie vom Baum herunter.
    In die Tüte von Papiere
    Sperren sie die Krabbeltiere.
    Fort damit und in die Ecke
    Unter Onkel Fritzens Decke!
    Bald zu Bett geht Onkel Fritze
    In der spitzen Zippelmütze;
    Seine Augen macht er zu,
    Hüllt sich ein und schläft in Ruh.
    Doch die Käfer, kratze, kratze!
    Kommen schnell aus der Matratze.
    Schon fasst einer, der voran,
    Onkel Fritzens Nase an.
    ,Bau!' - schreit er - Was ist das hier?!!"
    Und erfasst das Ungetier.
    Und den Onkel, voller Grausen,
    Sieht man aus dem Bette sausen.
    "Autsch!!" - Schon wieder hat er einen
    Im Genicke, an den Beinen;
    Hin und her und rundherum
    Kriecht es, fliegt es mit Gebrumm.
    Onkel Fritz, in dieser Not,
    Haut und trampelt alles tot
    Guckste wohl! Jetzt ist's vorbei
    Mit der Käferkrabbelei!
    Onkel Fritz hat wieder Ruh
    Und macht seine Augen zu.
    Dieses war der fünfte Streich,
    Doch der sechste folgt sogleich.```""",

    """
    ```In der schönen Osterzeit,
    Wenn die frommen Bäckersleut'
    'Viele süße Zuckersachen
    Backen und zurechte machen,
    Wünschten Max und Moritz auch
    Sich so etwas zum Gebrauch.
    Doch der Bäcker, mit Bedacht,
    Hat das Backhaus zugemacht.
    Also will hier einer stehlen,
    Muß er durch den Schlot sich quälen.
    Ratsch! Da kommen die zwei Knaben
    Durch den Schornstein, schwarz wie Raben.
    Puff! Sie fallen in die Kist',
    Wo das Mehl darinnen ist.
    Da! Nun sind sie alle beide
    Rundherum so weiß wie Kreide.
    Aber schon mit viel Vergnügen
    Sehen sie die Brezeln liegen.
    Knacks!! - Da bricht der Stuhl entzwei;
    Schwapp!! - Da liegen sie im Brei.```""",

    """
    ```Ganz von Kuchenteig umhüllt
    Stehn sie da als Jammerbild.
    Gleich erscheint der Meister Bäcker
    Und bemerkt die Zuckerlecker.
    Eins, zwei, drei! - Eh' man's gedacht,
    Sind zwei Brote draus gemacht.
    In dem Ofen glüht es noch -
    Ruff!! - damit ins Ofenloch!
    Ruff!! - man zieht sie aus der Glut;
    Denn nun sind sie braun und gut.
    jeder denkt, die sind perdü!
    Aber nein! - Noch leben sie!
    Knusper, knasper! - wie zwei Mäuse
    Fressen sie durch das Gehäuse;
    Und der Meister Bäcker schrie:
    "Ach herrje! Da laufen sie!"
    Dieses war der sechste Streich,
    Doch der letzte folgt sogleich.```""",

    """
    ```Max und Moritz, wehe euch!
    jetzt kommt euer letzter Streich!
    Wozu müssen auch die beiden
    Löcher in die Säcke schneiden??
    Seht, da trägt der Bauer Mecke
    Einen seiner Maltersäcke.
    Aber kaum dass er von hinnen,
    Fängt das Korn schon an zu rinnen.
    Und verwundert steht und spricht er:
    "Zapperment! Dat Ding werd lichter!"
    Hei! Da sieht er voller Freude
    Max und Moritz im Getreide.
    Rabs!! - in seinen großen Sack
    Schaufelt er das Lumpenpack.```""",

    """
    ```Max und Moritz wird es schwüle,
    Denn nun geht es nach der Mühle.
    ..Meister Müller, he, heran!
    Mahl er das, so schnell er kann!'
    ,Her damit!' Und in den Trichter
    Schüttet er die Bösewichter.
    Rickeracke! Rickeracke!
    Geht die Mühle 'mit Geknacke.
    Hier kann man sie noch erblicken,
    Fein geschroten und gebacken.
    Doch sogleich verzehret sie des
    Meister Müllers Federvieh. ```""",

    """
    ```Als man dies im Dorf erführ,
    War von Trauer keine Spur.
    Witwe Bolte, mild und weich,
    Sprach: "Sieh da, ich dacht,es gleich!"
    "jajaja!" rief Meister Böck
    "Bosheit ist kein Lebenszweck!"
    Drauf so sprach Herr Lehrer Lämpel:
    "Dies ist wieder ein Exempel!"
    "Freilich", meint' der Zuckerbäcker,
    "Warum ist der Mensch so lecker!-"
    Selbst der gute Onkel Fritze
    Sprach: "Das kommt von dumme Witze!"
    Doch der brave Bauersmann
    Dachte: Wat geiht meck dat an!
    Kurz, im ganzen Ort herum
    Ging ein freudiges Gebrumm:
    "Gott sei Dank! Nun ist's vorbei
    Mit der Übeltäterei!"```"""]
new_colossus = [
    """
    ```Not like the brazen giant of Greek fame,
    With conquering limbs astride from land to land;
    Here at our sea-washed, sunset gates shall stand
    A mighty woman with a torch, whose flame
    Is the imprisoned lightning, and her name
    Mother of Exiles. From her beacon-hand
    Glows world-wide welcome; her mild eyes command
    The air-bridged harbor that twin cities frame.
    “Keep, ancient lands, your storied pomp!” cries she
    With silent lips. “Give me your tired, your poor,
    Your huddled masses yearning to breathe free,
    The wretched refuse of your teeming shore.
    Send these, the homeless, tempest-tossed to me,
    I lift my lamp beside the golden door!”```"""]
road_not_taken = [
    """
    ```Two roads diverged in a yellow wood,
    And sorry I could not travel both
    And be one traveler, long I stood
    And looked down one as far as I could
    To where it bent in the undergrowth;```""",

    """
    ```Then took the other, as just as fair,
    And having perhaps the better claim,
    Because it was grassy and wanted wear;
    Though as for that the passing there
    Had worn them really about the same,```""",

    """
    ```And both that morning equally lay
    In leaves no step had trodden black.
    Oh, I kept the first for another day!
    Yet knowing how way leads on to way,
    I doubted if I should ever come back.```""",

    """
    ```I shall be telling this with a sigh
    Somewhere ages and ages hence:
    Two roads diverged in a wood, and I—
    I took the one less traveled by,
    And that has made all the difference.```"""]
ozymandias = [
    """
    ```I met a traveler from an antique land
    Who said: “Two vast and trunkless legs of stone
    Stand in the desert . . . Near them, on the sand,
    Half sunk, a shattered visage lies, whose frown,
    And wrinkled lip, and sneer of cold command,
    Tell that its sculptor well those passions read
    Which yet survive, stamped on these lifeless things,
    The hand that mocked them, and the heart that fed:
    And on the pedestal these words appear:
    ‘My name is Ozymandias, king of kings:
    Look on my works, ye Mighty, and despair!’
    Nothing beside remains. Round the decay
    Of that colossal wreck, boundless and bare
    The lone and level sands stretch far away.”```"""]
daffodils = [
    """
    ```I wandered lonely as a cloud
    That floats on high o’er vales and hills,
    When all at once I saw a crowd,
    A host, of golden daffodils;
    Beside the lake, beneath the trees,
    Fluttering and dancing in the breeze.```""",

    """
    ```Continuous as the stars that shine
    And twinkle on the milky way,
    They stretched in never-ending line
    Along the margin of a bay:
    Ten thousand saw I at a glance,
    Tossing their heads in sprightly dance.```""",

    """
    ```The waves beside them danced; but they
    Out-did the sparkling waves in glee:
    A poet could not but be gay,
    In such a jocund company:
    I gazed—and gazed—but little thought
    What wealth the show to me had brought:```""",

    """
    ```For oft, when on my couch I lie
    In vacant or in pensive mood,
    They flash upon that inward eye
    Which is the bliss of solitude;
    And then my heart with pleasure fills,
    And dances with the daffodils.```"""]
sonnet_18 = [
    """
    ```Shall I compare thee to a summer’s day?
    Thou art more lovely and more temperate:
    Rough winds do shake the darling buds of May,
    And summer’s lease hath all too short a date:
    Sometime too hot the eye of heaven shines,
    And often is his gold complexion dimm’d;
    And every fair from fair sometime declines,
    By chance, or nature’s changing course, untrimm’d;
    But thy eternal summer shall not fade
    Nor lose possession of that fair thou ow’st;
    Nor shall Death brag thou wander’st in his shade,
    When in eternal lines to time thou grow’st;
    So long as men can breathe or eyes can see,
    So long lives this, and this gives life to thee.```"""]
dulce_et_decorum = [
"""
```Bent double, like old beggars under sacks,
Knock-kneed, coughing like hags, we cursed through sludge,
Till on the haunting flares we turned our backs,
And towards our distant rest began to trudge.
Men marched asleep. Many had lost their boots,
But limped on, blood-shod. All went lame; all blind;
Drunk with fatigue; deaf even to the hoots
Of gas-shells dropping softly behind.```""",

"""
```Gas! GAS! Quick, boys!—An ecstasy of fumbling
Fitting the clumsy helmets just in time,
But someone still was yelling out and stumbling
And flound’ring like a man in fire or lime.
Dim through the misty panes and thick green light,
As under a green sea, I saw him drowning```""",

"""
```In all my dreams before my helpless sight,
He plunges at me, guttering, choking, drowning.```""",

"""
```If in some smothering dreams, you too could pace
Behind the wagon that we flung him in,
And watch the white eyes writhing in his face,
His hanging face, like a devil’s sick of sin;
If you could hear, at every jolt, the blood
Come gargling from the froth-corrupted lungs,
Obscene as cancer, bitter as the cud
Of vile, incurable sores on innocent tongues,—
My friend, you would not tell with such high zest
To children ardent for some desperate glory,
The old Lie: Dulce et decorum est
Pro patria mori.```"""
]

poems = [
    Literature("Edgar Allan Poe", "The Raven", the_raven, "the raven"),
    Literature("Edgar Allan Poe", "Annabel Lee", annabel_lee, "annabel lee"),
    Literature("Edgar Allan Poe", "For Annie", for_annie, "for annie"),
    Literature("Edgar Allan Poe", "Alone", alone, "alone"),
    Literature("Mary Elizabeth Frye", "Do Not Stand at My Grave and Weep", do_not_weep, "do not weep"),
    Literature("Elizabeth Bishop", "One Art", one_art, "one art"),
    Literature("William Blake", "The Tyger", the_tyger, "the tyger"),
    Literature("Robert Frost", "Stopping by Woods on a Snowy Evening", stopping_by_woods, "stopping by woods"),
    Literature("Emily Dickinson", "Much Madness is divinest Sense", much_madness, "much madness"),
    Literature("Alfred, Lord Tennyson", "The Charge of the Light Brigade", light_brigade, "light brigade"),
    Literature("Max Ehrmann", "Desiderata", desiderata, "desiderata"),
    Literature("Martin Niemöller", "First They Came", first_they_came, "first they came"),
    Literature("Kazi Nazrul Islam", "Kandari Hushiar", kandari_hushiar, "kandari hushiar"),
    Literature("Wilhelm Busch", "Max und Moritz", max_und_moritz, "max und moritz"),
    Literature("Emma Lazarus", "The New Colossus", new_colossus, "new colossus"),
    Literature("Robert Frost", "The Road Not Taken", road_not_taken, "road not taken"),
    Literature("Percy Bysshe Shelley", "Ozymandias", ozymandias, "ozymandias"),
    Literature("William Wordsworth", "Daffodils", daffodils, "daffodils"),
    Literature("William Shakespeare", "Sonnet 18", sonnet_18, "sonnet 18"),
    Literature("Wilfred Owen", "Dulce et Decorum est", dulce_et_decorum, "dulce et decorum")
]
poetry_index = """
```python
AUTHOR: "Edgar Allan Poe"
POEM:   "The Raven", "For Annie", "Annabel Lee", "Alone"
SYNTAX: "the raven", "for annie", "annabel lee", "alone"

AUTHOR: "Mary Elizabeth Frye"
POEM: "Do Not Stand At My Grave And Weep"
SYNTAX: "do not weep"

AUTHOR: "Robert Frost"
POEM: "Stopping By Woods On A Snowy Evening", "The Road Not Taken"
SYNTAX: "stopping by woods"

AUTHOR: "Elizabeth Bishop"
POEM: "One Art"
SYNTAX: "one art"

AUTHOR: "Emily Dickinson"
POEM: "Much Madness Is Divinest Sense"
SYNTAX: "much madness"

AUTHOR: "Alfred, Lord Tennyson"
POEM: "The Charge Of The Light Brigade"
SYNTAX: "light brigade"

AUTHOR: "William Blake"
POEM: "The Tyger"
SYNTAX: "the tyger"

AUTHOR: "Max Ehrmann"
POEM: "Desiderata"
SYNTAX: "desiderata"

AUTHOR: "Martin Niemöller"
POEM: "First They Came"
SYNTAX: "first they came"

AUTHOR: "Kazi Nazrul Islam"
POEM: "Karandi Hushiar"
SYNTAX: "karandi hushiar"

AUTHOR: "Wilhelm Busch"
POEM: "Max und Moritz"
SYNTAX: "max und moritz"

AUTHOR: "Emma Lazarus"
POEM: "The New Colossus"
SYNTAX: "new colossus"

AUTHOR: "William Wordsworth"
POEM: "Daffodils"
SYNTAX: "daffodils"

AUTHOR: "Percy Bysshe Shelley"
POEM: "Ozymandias"
SYNTAX: "daffodils"

AUTHOR: "William Shakespeare"
POEM: "Sonnet 18"
SYNTAX: "sonnet 18"

AUTHOR: "Wilfred Owen"
POEM: "Dulce et Decorum est"
SYNTAX: "dulce et decorum"```
"""
