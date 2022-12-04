import os

from django.http import HttpResponse
from config.settings import MEDIA_ROOT
from django.views.generic.edit import FormView

from .forms import EnterURL
from .logic import mp3_converter, file_remove


# NOTE: 随所にfile_removeを仕込んで、出来るだけファイルが残らないようにする
class YoutubeConverter(FormView):
    form_class = EnterURL
    template_name = 'youtube-converter.html'
    file_remove()

    def form_valid(self, form) -> HttpResponse:
        file_remove()
        urls = form.cleaned_data

        # NOTE: ここでYouTube動画をmp3に変換してmedia_rootに保存している
        convert = mp3_converter(urls)
        file_names = os.listdir(MEDIA_ROOT)

        if convert:
            message = convert  # 'URLを確認してください'というmessageになる
        else:
            message = "↓（変換後）クリックしてダウンロード" if len(file_names) != 0 else ''

        ctxt = self.get_context_data(form=form, file_names=file_names, message=message)

        return self.render_to_response(ctxt)
