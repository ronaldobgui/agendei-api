from abstract.scripts import ScriptsProvider

scripts = ScriptsProvider(source='scripts')

script = scripts.get('usuario.sql')

print(script)
