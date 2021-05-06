"""[summary]

[description]
"""

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import smart_str, smart_text
from django.conf import settings
import base64
from project.models import BaseModel, StackedModel


class MovieModel(StackedModel):
    """

    List<Genre> genre;
    int id;
    String image;
    List<Tag> tag;
    bool isHD;
    String logo;
    String avg_rating;
    String award_description;
    String censor_rating;
    String embed_content;
    String choice;
    String publish_date;
    String publish_date_gmt;
    String release_date;
    String run_time;
    String trailer_link;
    String url_link;
    String file;
    List<Visibility> visibility;
    bool isInWatchList;
    bool isLiked;
    int likes;
    String attachment;
    String award_image;
    List<RestrictSubscriptionPlan> restSubPlan;
    String restrict_user_status;
    RestrictionSetting restrictionSetting;
    dynamic imdb_rating;

    //video
    List<Genre> cat;
    String name_upcoming;
    bool is_featured;
    String cast;
    int views;

    PostType postType;"""

    title = models.CharField(max_length=512, verbose_name=_("Titulo"))
    description = models.TextField(verbose_name=_("Descrição"))
    excerpt = models.TextField(verbose_name=_("Resumo"))
    genres = models.ManyToManyField("movies.GenreModel")

    class Meta(StackedModel.Meta):
        verbose_name = _("Filme")
        verbose_name_plural = _("Filmes")

    def __str__(self):
        return self.title
