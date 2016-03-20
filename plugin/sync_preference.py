import os
import uuid
import pdb
import sublime
import sublime_plugin

from .configs import *

class SyncPreferencesCommand(sublime_plugin.TextCommand):

    settings = sublime.load_settings(SYNC_PREFERENCES_FILE)

    def sync_files(self):
        files_to_sync = self.get_files_to_sync()
        unique_id = uuid.uuid4()
        self.save_id(unique_id)
        print("saving for {0} with {1}".format(unique_id, files_to_sync))

    def get_files_to_sync(self):
        package_location = self.settings.get(USER_PACKAGE_LOCATION)
        exclude_files = self.settings.get(FILES_TO_EXCLUDE)
        files_to_sync = [ file
            for file in os.listdir(package_location)
            if os.path.isfile(os.path.join(package_location, file))
            and file not in exclude_files
            ]
        return files_to_sync

    def save_id(self, id):
        self.settings.set("unique_id", str(id))

    def run(self, edit):
        self.sync_files()
        sublime.save_settings(SYNC_PREFERENCES_FILE)
