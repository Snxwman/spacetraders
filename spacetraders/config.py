import tomlkit

class Config:

    def __init__(self, config_path):
        self._config_path = config_path
        raw_config = self._from_file()

        account_config = raw_config['account']
        self.token: str = str(account_config['token'])
        self.email: str = str(account_config['email'])

    def _from_file(self):
        with open(self._config_path) as config_file:
            return tomlkit.load(config_file)

CONFIG = Config('config.toml')
