class UsertRouter:
    route_app_labels = ['auth', 'contenttypes', 'admin', 'sessions']

    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return "user_db"
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return "user_db"
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label in self.route_app_labels or obj2._meta.app_label in self.route_app_labels:
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in self.route_app_labels:
            return db == "user_db"
        return None

class PostRouter:
    route_app_labels = ['post', 'poll', 'category', 'django_summernote']

    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return "post_db"
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return "post_db"
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label in self.route_app_labels or obj2._meta.app_label in self.route_app_labels:
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in self.route_app_labels:
            return db == "post_db"
        return None

class AdvertisingRouter:
    route_app_labels = ['advertising']

    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return "advertising_db"
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return "advertising_db"
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label in self.route_app_labels or obj2._meta.app_label in self.route_app_labels:
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in self.route_app_labels:
            return db == "advertising_db"
        return None

class PresentationRouter:
    route_app_labels = ['presentation']

    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return "presentation_db"
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return "presentation_db"
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label in self.route_app_labels or obj2._meta.app_label in self.route_app_labels:
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in self.route_app_labels:
            return db == "presentation_db"
        return None
