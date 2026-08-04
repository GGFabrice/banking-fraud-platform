from cleaning import CleaningPipeline

pipeline = CleaningPipeline(
    input_folder="data/raw",
    output_folder="data/cleansed"
)

pipeline.run()