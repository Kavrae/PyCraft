# TODO change to a status effect factory
# have various parts of status effects which it pieces together on-demand to build different effects

class StatusEffect:
    _name = None
    _start_duration = None
    _ticks_remaining = None

    _can_stack = None

    def run(self):
        print("Run is not implemented")

    # As opposed to init, which is used for default values, use on_added for character-specific effects for adding it
    # Such as resistance or immunity to specific effects
    def on_added(self):
        print("On Added not implemented")

    def on_removed(self):
        print("On Removed not implemented")