library(tesseract)
library(furrr)
library(yyjsonr)
library(tictoc)
library(stringi)
library(fs)


# set-up ------------------------------------------------------------------

# Let's set up a few things 
input_dir <- 'transcripts/STUREC_HS/'
output_dir <- 'transcripts/json_ocr_sturec'

# create output json directory if it doesn't exist;
# will not overwrite existing directory
if(!dir.exists(output_dir)){
  dir.create(output_dir)
}


# comparing files that were processed and those that need to be processed
files_processed <- list.files(output_dir) |> 
  path_ext_remove()  

files_to_be_processed <-  list.files(input_dir) |>
  path_ext_remove()


files_delta <- setdiff(files_to_be_processed,files_processed)



# preparing inputs for OCR
input_files <- path(input_dir,files_delta)
target <- dir_ls(input_dir)
index <- pmatch(input_files, target)
input_files <- target[index]

output_files <- path(output_dir, files_delta,ext='json')


# perform ocr -------------------------------------------------------------

plan(multisession)


tic()

future_pmap(list(input_files, output_files, files_delta),
                   function(x, y, z){
                     temp <- ocr(x)
                     write_json_file(list(id = z,data = temp),y)
                     
                   },
                            .progress=TRUE, 
                            .options = furrr_options(seed = 123))
toc()
