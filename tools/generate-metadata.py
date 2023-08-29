#!/bin/env python3
import glob
import frontmatter
import yaml

projects_metadata = dict()
publications_metadata = dict()


def get_project_files() -> list:
    markdown_files = glob.glob("./docs/projects/*.md")
    return markdown_files


def get_publication_files() -> list:
    markdown_files = glob.glob("./docs/publications/*.md")
    return markdown_files


def parse_all_files():
    for filename in get_project_files():
        try:
            if '_index.md' in filename:
                continue
            post = frontmatter.load(filename)
            projects_metadata[post.metadata['key']] = post.metadata
            projects_metadata[post.metadata['key']]['path'] = str(filename)
            projects_metadata[post.metadata['key']]['url'] = str(filename).replace('./docs/', './')
            print(f'- parsed: "{filename}"')
        except:
            print(f'! error: "{filename}"')
    for filename in get_publication_files():
        try:
            if '_index.md' in filename:
                continue
            post = frontmatter.load(filename)
            publications_metadata[post.metadata['key']] = post.metadata
            publications_metadata[post.metadata['key']]['path'] = str(filename)
            publications_metadata[post.metadata['key']]['url'] = str(filename).replace('./docs/', './')
            print(f'- parsed: "{filename}"')
        except:
            print(f'! error: "{filename}"')


if __name__ == '__main__':
    parse_all_files()
    print('generate-metadata')
    with open('data/projects_metadata_gen.yml', 'w') as file:
        yaml.dump(projects_metadata, file)

    with open('data/publications_metadata_gen.yml', 'w') as file:
        yaml.dump(publications_metadata, file)
