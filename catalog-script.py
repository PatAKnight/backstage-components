import os
import random
import yaml
import argparse

FRUITS = ["apple", "banana", "cherry", "grapefruit", "strawberry", "plum", "raspberry", "mango", "pineapple", "papaya", "blueberry", "pomegranate", "guava", "orange", "apricot", "watermelon", "peach", "pear", "blackberry", "lime", "date", "elderberry", "fig", "grape", "kiwi", "lemon", "cantaloupe", "melon", "breadfruit", "starfruit"]

VEGETABLES = ["carrots", "peas", "tomatoes", "onions", "peppers", "mushrooms", "cucumbers", "gourds", "leeks", "parsnips", "potatoes", "pumpkins", "shallots", "zucchinis", "turnips"]

MAMMALS = ["elephant", "lion", "giraffe", "whale", "dolphin", "koala", "panda", "cheetah", "zebra", "kangaroo", "gorilla", "rhinoceros", "hippopotamus", "bat", "orangutan", "sloth", "tiger", "lemur", "wolf", "fox"]

SNAKES = ["anaconda", "python", "cobra", "viper", "boa-constrictor", "garter-snake", "king-cobra", "rattlesnake", "black-mamba", "green-tree-python", "corn-snake", "ball-python", "rat-snake", "gopher-snake", "indigo-snake", "water-snake", "boomslang", "milk-snake", "sea-snake", "pit-viper"]

FISH = ["salmon", "trout", "tuna", "cod", "bass", "catfish", "perch", "goldfish", "guppy", "swordfish", "mackerel", "anchovy", "halibut", "carp", "anglerfish", "pufferfish", "clownfish", "seahorse", "sturgeon", "arowana"]

BIRDS = ["sparrow", "eagle", "hawk", "owl", "penguin", "parrot", "robin", "flamingo", "toucan", "hummingbird", "peacock", "swan", "pelican", "vulture", "woodpecker", "kingfisher", "crow", "magpie", "canary", "blue-jay"]

API_TYPES = ["openapi", "grpc", "trpc", "asyncapi", "graphql"]

RESOURCE_TYPES = ["database", "gitops", "identity-provider", "repository", "s3", ""]

COMPONENT_TYPES = ["website", "service", "library"]

LIFECYCLE = ["production", "experimental", "deprecated"]

GROUP_FOLDER_STRUCTURE = "catalog-entities/large-org/groups"
USER_FOLDER_STRUCTURE = "catalog-entities/large-org/users"
API_FOLDER_STRUCTURE = "catalog-entities/large-org/apis"
SYSTEM_FOLDER_STRUCTURE = "catalog-entities/large-org/systems"
RESOURCES_FOLDER_STRUCTURE = "catalog-entities/large-org/resources"
COMPONENTS_FOLDER_STRUCTURE = "catalog-entities/large-org/components"
LOCATION_FOLDER_STRUCTURE = "catalog-entities/large-org/"

GROUP_CHOICES = []
SYSTEM_CHOICES = []
RESOURCE_CHOICES = []
API_CHOICES = []
COMPONENT_CHOICES = []
USER_CHOICES = []
LOCATIONS = ["users", "groups", "apis", "systems", "resources", "components"]
LOCATIONS_CHOICES = [USER_CHOICES, GROUP_CHOICES, API_CHOICES, SYSTEM_CHOICES, RESOURCE_CHOICES, COMPONENT_CHOICES]

def generate_random_name(items):
  return random.choice(items)

def generate_user_yaml_content(name, number, group_name, group_number):
  memberOf = [f"{group_name}-{group_number}"]
  content = {
      "apiVersion": "backstage.io/v1alpha1",
      "kind": "User",
      "metadata": {
          "name": f"{name.lower()}-{number}"
      },
      "spec": {
          "profile": {
              "email": f"{name.lower()}-{number}@example.com",
              "displayName": f"{name.capitalize()} {number}"
          },
          "memberOf": memberOf
      }
  }
  return yaml.dump(content)

def generate_group_yaml_content(name, number):
  content = {
      "apiVersion": "backstage.io/v1alpha1",
      "kind": "Group",
      "metadata": {
          "name": f"{name.lower()}-{number}",
          "title": f"{name.capitalize()} {number}"
      },
      "spec": {
          "type": "team",
          "children": "[]"
      }
  }
  return yaml.dump(content)

def generate_api_yaml_content(name, number, type_choice, system, group, group_number, lifecycle):
  content = {
      "apiVersion": "backstage.io/v1alpha1",
      "kind": "API",
      "metadata": {
          "name": f"{name.lower()}-{number}",
          "title": f"{name.capitalize()} {number}",
          "description": f"{name.lower()}-{number} basic description that is used as an example for an API"
      },
      "spec": {
          "type": f"{type_choice}",
          "system": f"{system}",
          "owner": f"{group}-{group_number}",
          "lifecycle": f"{lifecycle}"
      }
  }
  return yaml.dump(content)

def generate_system_yaml_content(name, number, group, group_number):
  content = {
      "apiVersion": "backstage.io/v1alpha1",
      "kind": "System",
      "metadata": {
          "name": f"{name.lower()}-{number}",
          "title": f"{name.capitalize()} {number}",
      },
      "spec": {
          "owner": f"{group}-{group_number}",
      }
  }
  return yaml.dump(content)

def generate_resource_yaml_content(name, number, type_choice, system, group, group_number, lifecycle):
  content = {
      "apiVersion": "backstage.io/v1alpha1",
      "kind": "Resource",
      "metadata": {
          "name": f"{name.lower()}-{number}",
          "title": f"{name.capitalize()} {number}",
          "description": f"{name.lower()}-{number} basic description that is used as an example for a Resource"
      },
      "spec": {
          "type": f"{type_choice}",
          "system": f"{system}",
          "owner": f"{group}-{group_number}",
          "lifecycle": f"{lifecycle}"
      }
  }
  return yaml.dump(content)

def generate_component_yaml_content(name, number, type_choice, system, group, group_number, lifecycle, resources, sub_components, consumes_apis):
  random_resources = random.sample(resources, 2)
  random_sub_component = random.sample(sub_components, 1)
  random_consumes_apis = random.sample(consumes_apis, 2)

  content = {
    "apiVersion": "backstage.io/v1alpha1",
    "kind": "Component",
    "metadata": {
        "name": f"{name.lower()}-{number}",
        "title": f"{name.capitalize()} {number}",
        "description": f"{name.lower()}-{number} basic description that is used as an example for a Component",
        "annotations": {
          "argocd/app-name": f"{name.lower()}-{number}",
          "backstage.io/kubernetes-id": f"{name.lower()}-{number}",
          "backstage.io/kubernetes-namespace": f"{system}",
        },
    },
    "spec": {
        "type": f"{type_choice}",
        "system": f"{system}",
        "owner": f"{group}-{group_number}",
        "lifecycle": f"{lifecycle}",
        "dependOns": random_resources
    }
  }

  # Randomly include providesApis, consumesApis, subcomponentOf. 1/3 chance
  if random.choice([True, False, False]):
    content["spec"]["providesApis"] = [f"{name.lower()}-{number}"]

  if random.choice([True, False, False]):
    content["spec"]["consumesApis"] = random_consumes_apis

  if random.choice([True, False, False]):
    content["spec"]["subcomponentOf"] = random_sub_component
  return yaml.dump(content)

def generate_location_yaml_content(name, resources):
  folder = f"/{name}/"
  ex = ".yaml"
  for i in range(len(resources)):
      resources[i] = f"{folder}{resources[i]}{ex}"

  folder = f"/{name}/"
  ex = ".yaml"
  content = {
      "apiVersion": "backstage.io/v1alpha1",
      "kind": "Location",
      "metadata": {
          "name": f"{name.lower()}",
          "description": f"A collection of all {name.lower()}"
      },
      "spec": {
          "targets": resources
      }
  }
  return yaml.dump(content)

def save_yaml_file(name, content, number, folder_structure, location):
  if (location):
    filename = f"{folder_structure}/{name.lower()}.yaml"
  else:
    filename = f"{folder_structure}/{name.lower()}_{number}.yaml"
  os.makedirs(os.path.dirname(filename), exist_ok=True)
  with open(filename, "w") as file:
      file.write(content)

def create_resources(args):
  for group_number in range(args.groups):
      vegetable_name = generate_random_name(VEGETABLES)
      group_yaml_content = generate_group_yaml_content(vegetable_name, group_number)
      save_yaml_file(vegetable_name, group_yaml_content, group_number, GROUP_FOLDER_STRUCTURE, False)
      GROUP_CHOICES.append(f"{vegetable_name}-{group_number}")

      for system_number in range(args.systems):
        snake_name = generate_random_name(SNAKES)
        system_yaml_content = generate_system_yaml_content(snake_name, system_number, vegetable_name, group_number)
        save_yaml_file(snake_name, system_yaml_content, system_number, SYSTEM_FOLDER_STRUCTURE, False)
        SYSTEM_CHOICES.append(f"{snake_name}-{system_number}")

      for api_number in range(args.apis):
        mammal_name = generate_random_name(MAMMALS)
        type_choice = generate_random_name(API_TYPES)
        system_choice = generate_random_name(SYSTEM_CHOICES)
        lifecycle_choice = generate_random_name(LIFECYCLE)

        api_yaml_content = generate_api_yaml_content(mammal_name, api_number, type_choice, system_choice, vegetable_name, group_number, lifecycle_choice)
        save_yaml_file(mammal_name, api_yaml_content, api_number, API_FOLDER_STRUCTURE, False)
        API_CHOICES.append(f"{mammal_name}-{api_number}")

      for resource_number in range(args.resources):
        fish_name = generate_random_name(FISH)
        type_choice = generate_random_name(RESOURCE_TYPES)
        system_choice = generate_random_name(SYSTEM_CHOICES)
        lifecycle_choice = generate_random_name(LIFECYCLE)

        resource_yaml_content = generate_resource_yaml_content(fish_name, resource_number, type_choice, system_choice, vegetable_name, group_number, lifecycle_choice)
        save_yaml_file(fish_name, resource_yaml_content, resource_number, RESOURCES_FOLDER_STRUCTURE, False)
        RESOURCE_CHOICES.append(f"resource:{fish_name}-{resource_number}")

      for component_number in range(args.components):
        bird_name = generate_random_name(BIRDS)
        type_choice = generate_random_name(COMPONENT_TYPES)
        system_choice = generate_random_name(SYSTEM_CHOICES)
        lifecycle_choice = generate_random_name(LIFECYCLE)
        COMPONENT_CHOICES.append(f"{bird_name}-{component_number}")

        component_yaml_content = generate_component_yaml_content(fish_name, component_number, type_choice, system_choice, vegetable_name, group_number, lifecycle_choice, RESOURCE_CHOICES, COMPONENT_CHOICES, API_CHOICES)
        save_yaml_file(bird_name, component_yaml_content, component_number, COMPONENTS_FOLDER_STRUCTURE, False)

      for user_number in range(args.users):
        fruit_name = generate_random_name(FRUITS)
        user_yaml_content = generate_user_yaml_content(fruit_name, user_number, vegetable_name, group_number)
        save_yaml_file(fruit_name, user_yaml_content, user_number, USER_FOLDER_STRUCTURE, False)
        USER_CHOICES.append(f"{fruit_name}-{user_number}")

  for i in range(len(LOCATIONS)):
    location_yaml_content = generate_location_yaml_content(LOCATIONS[i], LOCATIONS_CHOICES[i])
    save_yaml_file(LOCATIONS[i], location_yaml_content, 1, LOCATION_FOLDER_STRUCTURE, True)


def main():
  parser = argparse.ArgumentParser(description="Your script description")
  parser.add_argument("-g", "--groups", type=int, default=15, help="Number of Groups")
  parser.add_argument("-u", "--users", type=int, default=2, help="Number of Users")
  parser.add_argument("-a", "--apis", type=int, default=2, help="Number of APIs")
  parser.add_argument("-c", "--components", default=2, type=int, help="Number of Components")
  parser.add_argument("-r", "--resources", default=3, type=int, help="Number of Resources")
  parser.add_argument("-s", "--systems", default=2, type=int, help="Number of Systems")

  args = parser.parse_args()
  create_resources(args)

if __name__ == "__main__":
   main()