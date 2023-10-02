from django.contrib.admin import site, ModelAdmin
from .models.research import Research
from .models.work_request import WorkRequest

class ResearchModelAdmin(ModelAdmin):
    pass

class WorkRequestModelAdmin(ModelAdmin):
    pass

site.register(Research, ResearchModelAdmin)
site.register(WorkRequest,WorkRequestModelAdmin)