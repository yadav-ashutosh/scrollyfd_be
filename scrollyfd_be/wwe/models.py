from django.db import models

class MediaSource(models.Model):
    title = models.CharField(max_length=255)  # Title of the video/media
    link = models.URLField()  # The link to the video/media
    description = models.TextField(blank=True, null=True)  # Optional description
    
    # Store the source as a comma-separated string for SQLite3 compatibility
    source = models.CharField(max_length=255)  # Example: "YouTube, Amazon Prime"
    
    likes = models.IntegerField(default=0)  # Count of likes
    dislikes = models.IntegerField(default=0)  # Count of dislikes

    def __str__(self):
        return self.title

    def get_sources_list(self):
        """
        Return the sources as a list by splitting the comma-separated string.
        """
        return self.source.split(', ')

    def set_sources_list(self, source_list):
        """
        Set the sources as a comma-separated string from a list.
        """
        self.source = ', '.join(source_list)
