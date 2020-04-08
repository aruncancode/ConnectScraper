# string = """English - Semester 1 Dorinda Walsh Semester 1 Cumulative Percent
#             Year 10 English Raw Score Weighted Mark
#             Short Response to Poetry Raw Score Weighted Mark 15O Out of 20 5.6 Out of 7.5
#             Novel Essay Raw Score Weighted Mark-Out of 40-Out of 10
#             Documentary Oral Presentation Raw Score Weighted Mark-Out of 40-Out of 7.5
#             Semester 1 Examination Raw Score Weighted Mark-Out of 60-Out of 15"""
# print(string)
# string = string.replace("Created with Highstock 4.2.6", "")
# raw_mark = string.split("Weighted Mark")
# weighted_mark = string.split("Raw Score")
# subject = string.split("-")[0]
# name = raw_mark

db = {}

english_string = "Year 10 EnglishRaw ScoreWeighted MarkShort Response to PoetryRaw ScoreWeighted Mark15Out of 205.6Out of 7.5Novel EssayRaw ScoreWeighted Mark-Out of 40-Out of 10Documentary Oral PresentationRaw ScoreWeighted Mark-Out of 40-Out of 7.5Semester 1 ExaminationRaw ScoreWeighted Mark-Out of 60-Out of 15"
pe_string = "Yr 10 PE OnlyRaw ScoreWeighted MarkPhysical EducationSkills, concepts and match play in a selected sportRaw ScoreWeighted Mark-Out of 10-Out of 18.75Raw ScoreWeighted Mark-Out of 10-Out of 6.25Skills, concepts and match play in a selected sportRaw ScoreWeighted Mark-Out of 10-Out of 18.75Raw ScoreWeighted Mark-Out of 10-Out of 6.25"


def format(string):
    string = string.replace("Raw Score", " Raw Score ")
    string = string.replace("Weighted Mark", " Weighted Mark ")
    raw_split = string.split("Raw Score")
    weighted_split = string.split("Weighted Mark")
    return weighted_split


print(format(english_string))


# assesment_title = None

# db["title"] = assesment_title
# db["raw_mark"] = 0
# db["weighted_mark"] = 0
# db["percentage"] = 0
# db["subject"] = 0

# print(db)
