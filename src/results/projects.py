import pandas as pd

naa_chrome = pd.read_csv('../chromium/NAA/naa.out', header=None, names=['hash', 'naa'], sep=':')
naa_linux = pd.read_csv('../linux/NAA/naa.out', header=None, names=['hash', 'naa'], sep=':')
naa_ffmpeg = pd.read_csv('../ffmpeg/NAA/naa.out', header=None, names=['hash', 'naa'], sep=':')
naa_imagemagick = pd.read_csv('../ImageMagick/NAA/naa.out', header=None, names=['hash', 'naa'], sep=':')

pic_chrome = pd.read_csv('../chromium/PSC/psc.out', header=None, names=['hash', 'psc'], sep=':')
pic_linux = pd.read_csv('../linux/PSC/psc.out', header=None, names=['hash', 'psc'], sep=':')
pic_ffmpeg = pd.read_csv('../ffmpeg/PSC/psc.out', header=None, names=['hash', 'psc'], sep=':')
pic_imagemagick = pd.read_csv('../ImageMagick/PSC/psc.out', header=None, names=['hash', 'psc'], sep=':')

nea_chrome = pd.read_csv('../chromium/NEA/is-nea.out', header=None, names=['hash', 'nea'], sep=':')
nea_linux = pd.read_csv('../linux/NEA/is-nea.out', header=None, names=['hash', 'nea'], sep=':')
nea_ffmpeg = pd.read_csv('../ffmpeg/NEA/is-nea.out', header=None, names=['hash', 'nea'], sep=':')
nea_imagemagick = pd.read_csv('../ImageMagick/NEA/is-nea.out', header=None, names=['hash', 'nea'], sep=':')

cc_chrome = pd.read_csv('../chromium/code_churn/code_churn.out', header=None, names=['hash', 'code_churn'], sep=':')
cc_linux = pd.read_csv('../linux/code_churn/code_churn.out', header=None, names=['hash', 'code_churn'], sep=':')
cc_ffmepg = pd.read_csv('../ffmpeg/code_churn/code_churn.out', header=None, names=['hash', 'code_churn'], sep=':')
cc_imagemagick = pd.read_csv('../ImageMagick/code_churn/code_churn.out', header=None, names=['hash', 'code_churn'], sep=':')

fc_chrome = pd.read_csv('../chromium/file_churn/file_churn.out', header=None, names=['hash', 'file_churn'], sep=':')
fc_linux = pd.read_csv('../linux/file_churn/file_churn.out', header=None, names=['hash', 'file_churn'], sep=':')
fc_ffmepg = pd.read_csv('../ffmpeg/file_churn/file_churn.out', header=None, names=['hash', 'file_churn'], sep=':')
fc_imagemagick = pd.read_csv('../ImageMagick/file_churn/file_churn.out', header=None, names=['hash', 'file_churn'], sep=':')

ncb_chrome = pd.read_csv('../pesquisa-es/githubapi/logs/chrome-vfcs/commits_by_author_2023-04-07_08:47:33_-0300.csv', header=None, names=['hash', 'ncb', 'author'], sep=';')
ncb_linux = pd.read_csv('../pesquisa-es/githubapi/logs/linux-vfcs/commits_by_author_2023-04-08_04:23:24_-0300.csv', header=None, names=['hash', 'ncb', 'author'], sep=';')
ncb_ffmepg = pd.read_csv('../pesquisa-es/githubapi/logs/ffmpeg-vfcs/commits_by_author_2023-04-06_08:27:36_-0300.csv', header=None, names=['hash', 'ncb', 'author'], sep=';')
ncb_imagemagick = pd.read_csv('../pesquisa-es/githubapi/logs/image-magick-vfcs/commits_by_author_2023-04-06_09:05:14_-0300.csv', header=None, names=['hash', 'ncb', 'author'], sep=';')

projects = [
  {
    'name':'Chromium',
    'naa': naa_chrome,
    'psc': pic_chrome,
    'nea': nea_chrome,
    'code_churn': cc_chrome,
    'file_churn': fc_chrome,
    'ncb': ncb_chrome,
  },
  {
    'name':'Linux',
    'naa': naa_linux,
    'psc': pic_linux,
    'nea': nea_linux,
    'code_churn': cc_linux,
    'file_churn': fc_linux,
    'ncb': ncb_linux,
  },
  {
    'name':'FFmpeg',
    'naa': naa_ffmpeg,
    'psc': pic_ffmpeg,
    'nea': nea_ffmpeg,
    'code_churn': cc_ffmepg,
    'file_churn': fc_ffmepg,
    'ncb': ncb_ffmepg,
  },
  {
    'name':'ImageMagick',
    'naa': naa_imagemagick,
    'psc': pic_imagemagick,
    'nea': nea_imagemagick,
    'code_churn': cc_imagemagick,
    'file_churn': fc_imagemagick,
    'ncb': ncb_imagemagick,
  },
]