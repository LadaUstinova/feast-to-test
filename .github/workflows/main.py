name: Applying features
on: [push]
jobs:
  Feast-apply:
    runs-on: self-hosted
    steps:
      - run: echo "Start applying features into Feast"
      - name: Check out repository code
        uses: actions/checkout@v2
      - run: feast apply
      - run: echo ":green_apple: This job's status is ${{ job.status }}."
