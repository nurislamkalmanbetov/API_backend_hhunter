# from django.utils import timezone
# from datetime import date
# from docx import Document
# from docx.shared import Pt
# import os

# class CVGenerator:
#     def __init__(self, profile):
#         self.profile = profile

#         self.dt = timezone.localtime()
#         self.today = date.today()

#         self.BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__).replace('/applications', '')))
#         self.COMMON_PATH = os.path.join(self.BASE_PATH, 'common_docs/')
#         self.MEDIA_PATH = os.path.join(self.BASE_PATH, 'media/')

#         self.DEFAUL_DIRECTORY = f'{self.COMMON_PATH}documents/'
#         self.OUTPUT_DIRECTORY = f'{self.MEDIA_PATH}documents/'

#     def generate_filename(self):
#         filename = f'{self.DEFAUL_DIRECTORY}cv.docx'
#         output_filename = f'{self.OUTPUT_DIRECTORY}{self.profile.last_name}-{self.profile.first_name}-cv.docx'
#         return filename, output_filename

#     # Остальные методы остаются без изменений

#     def generate_cv(self):
#         if self.profile.is_confirmed and self.profile.is_admin_confirmed and self.profile.is_form_completed \
#                     and self.profile.photo_for_schengen:
#             filename, output_filename = self.generate_filename()
#             self.generate_document(filename, output_filename)
#             return output_filename
#         return None