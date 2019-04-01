import save
import uvid

uvid = uvid.getuvid()
file_name = str(uvid)+'.csv'

save.createfile(file_name)
