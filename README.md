# Book Recommender

## Development

- first you might need to download CSV dump from datasource link in resource into `/notebooks/data` dir
- to start collaborative filtering `make nb-up` with optional `make nb-build` if not built yet
- to start streamlit backend `make be-bash` / `make be-up` with optional `make be-build`

## Production

- to spin up infrastructure `terraform apply terraform/`
- to build and tag image `make be-prod-build`
- to push to ecr `make be-prod-push`

## Resources

- [Datasource](http://www2.informatik.uni-freiburg.de/~cziegler/BX/)

Code heavily inspider by following sources

- [Keras official collaborative filtering example](https://keras.io/examples/structured_data/collaborative_filtering_movielens/)
- [Deep learning Cookbook](https://github.com/DOsinga/deep_learning_cookbook)
- [Bradford Hamilton's article about ECS](https://medium.com/@bradford_hamilton/deploying-containers-on-amazons-ecs-using-fargate-and-terraform-part-2-2e6f6a3a957f)
- [And his repo](https://github.com/bradford-hamilton/terraform-ecs-fargate)