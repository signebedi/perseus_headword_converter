import click
from beta_conv.mapping import beta_code_mapping


@click.command()
@click.argument('greek_text')
def greek_to_beta_code(greek_text):
    """Converts a Greek word to its Beta Code representation."""

    # Convert the Greek word to Beta Code
    beta_code_word = ''.join(beta_code_mapping[char] for char in greek_text if char in beta_code_mapping)

    click.echo(f'Beta Code for "{greek_text}": {beta_code_word}')

if __name__ == '__main__':
    greek_to_beta_code()
