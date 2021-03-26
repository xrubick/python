import click

@click.command()
@click.option('--count', default=1, help='number of greetings')
@click.argument('name')
def hello(count, name):
    for x in range(count):
        click.echo('Hello %s!' % name)
##
#@click.command()
#def hello():
#    click.echo('Hello World')

@click.group()
def cli():
    pass

@cli.command()
@click.option('--count', default=1, help='number of greetings')
@click.argument('name')
def init_db(count,name):
    for x in range(count):
        click.echo('Initialized the %s database' % name)

@cli.command()
def drop_db():
    click.echo('Dropped the database')
##
#@click.command()
#def initdb():
#    click.echo('Initialized the database')
#
#@click.command()
#def dropdb():
#    click.echo('Dropped the database')
#
#cli.add_command(initdb)
#cli.add_command(dropdb)

if __name__ == '__main__':
    hello()
