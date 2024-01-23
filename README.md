<h3 id="1" align="center">Clone project</h3>

```sh
git clone git@github.com:Deyvidas/remove_suffix_in_file_names.git
cd remove_suffix_in_file_names
poetry env use python[version]
```

---

<h3 id="2" align="center">Add the root directory of the project, to the activate script</h3>

```bash
# remove_suffix_in_file_names/.venv/bin/activate
...
PYTHONPATH="/absolute/path/to/remove_suffix_in_file_names"
export PYTHONPATH
...
```

---

<h3 id="3" align="center">Install all necessary dependencies</h3>

```sh
poetry shell

# You can check if the PYTHONPATH is exported:
echo $PYTHONPATH
/absolute/path/to/remove_suffix_in_file_names

poetry install
```

---

<h3 id="3" align="center">How to use script</h3>

Now that the project is ready, you can run the script.

<details><br><summary><b></b>Files names before script:</summary>

```sh
remove_suffix_in_file_names/lib/
├── bootstrap-datepicker/
│   ├── css/
│   │   ├── bootstrap-datepicker.min.css?v=nx7SjIq6Ec0mq8-0Zx5PAgGuYdcYMvpyzuPJCr7q6YI
│   │   └── bootstrap-datepicker.standalone.min.css?v=8_PcxkdmqjNGUzE0-tw_RWqI-IAG8-ybXiYBfyHTPbo
│   ├── js/
│   │   └── bootstrap-datepicker.min.js?v=wSn1lWvI6cOig4Bp6aP_UK16VAoHe0KTSyxdfJAvTvw
│   └── locales/
│       └── bootstrap-datepicker.ru.min.js?v=iGDUwn2IPSzlnLlVeCe3M4ZIxQxjUoDYdEO6oBZw_Go
├── esri-leaflet-geocoder/
│   └── esri-leaflet-geocoder.min.js
├── fancybox/
│   ├── jquery.fancybox.min.css
│   └── jquery.fancybox.min.js?v=HALK8qDxYxiWVnb9SyZSZXKNZPuieUogsHFRpOiR_KY
├── jquery/
│   └── dist/
│       └── jquery.min.js?v=82hEkGrSMJh3quMSG4f7FbngmAPLTDM63H4eNayS4Us
├── jquery-validation/
│   └── dist/
│       └── jquery.validate.min.js?v=6e0N-WJiVKBeTitK1GKSwPi3rbdPpLtuqaiitZjeD2w
├── jquery-validation-unobtrusive/
│   └── jquery.validate.unobtrusive.min.js?v=9GycpJnliUjJDVDqP0UEu_bsm9U-3dnQUH8-3W10vkY
├── leaflet/
│   ├── images/
│   │   ├── layers-2x.png
│   │   ├── layers.png
│   │   └── marker-icon.png
│   ├── leaflet.css
│   └── leaflet.js
├── leaflet-geosearch/
│   ├── esri-leaflet.js
│   └── geosearch.umd.min.js
├── leaflet.markercluster/
│   └── leaflet.markercluster.js
├── moveto/
│   └── move-to.min.js?v=KVPBMr_w1-u_gSR6nGm3zdcBP_Q25nR56msdhqv6H1M
├── my-custom-scrollbar/
│   ├── jquery.mCustomScrollbar.css?v=FzDSfCZaTH7qcj5EpRUsb98KPowD0alLR7LhpZSRfqU
│   └── jquery.mCustomScrollbar.js?v=EzmsVDqHl8jBItF1U5XGby3Djd92u8y6A9blx7B7nk4
├── object-fit-ie/
│   └── object-fit-ie.js?v=ON-dQ8J7QTPwUiPy2U4n25Uf31PD25-RvL_Gz44IEEo
├── select2/
│   ├── css/
│   │   └── select2.css?v=f6ld2Ni1kE88xxjBrdMt2It8M6ps4nX0P4rXAnvltWo
│   └── js/
│       ├── i18n/
│       └── select2.min.js?v=70QcFVMi3-VGiAVSY1KGFibayMynhoK4aX6BVJErm00
├── slick/
│   ├── fonts/
│   │   ├── slick.eot
│   │   ├── slick.eot?
│   │   ├── slick.svg
│   │   ├── slick.ttf
│   │   └── slick.woff
│   ├── ajax-loader.gif
│   ├── slick.css?v=8LcixIxSCCzXcmFXTiKlJR_jfqSykbFEETQUW6ubIGM
│   ├── slick.min.js?v=4aUsCgb6n2XgFbAufsRj_WISEanSrkS2ZgWXkA6Sf7s
│   └── slick-theme.css?v=B4eGwVoXYEh3pKqquJGr_QHz3FcrGtGRmSS8izz2AAk
└── unobtrusive-ajax/
    └── jquery.unobtrusive-ajax.js?v=54TsJTD6nXoHGcft9-SPH4jgcV_3ayinJaWSmiPWYME

25 directories, 34 files
```

<hr style="margin-left: 25%; margin-right: 25%;"></details>

```sh
python main.py
? Please enter the path of dir. /absolute/path/to/remove_suffix_in_file_names/lib/
```

<details><br><summary><b></b>All the names of the files that were renamed are printed.</summary>

```sh
original: /absolute/path/to/remove_suffix_in_file_names/lib/object-fit-ie/object-fit-ie.js?v=ON-dQ8J7QTPwUiPy2U4n25Uf31PD25-RvL_Gz44IEEo
replaced: /absolute/path/to/remove_suffix_in_file_names/lib/object-fit-ie/object-fit-ie.js

original: /absolute/path/to/remove_suffix_in_file_names/lib/slick/slick.min.js?v=4aUsCgb6n2XgFbAufsRj_WISEanSrkS2ZgWXkA6Sf7s
replaced: /absolute/path/to/remove_suffix_in_file_names/lib/slick/slick.min.js

original: /absolute/path/to/remove_suffix_in_file_names/lib/slick/slick.css?v=8LcixIxSCCzXcmFXTiKlJR_jfqSykbFEETQUW6ubIGM
replaced: /absolute/path/to/remove_suffix_in_file_names/lib/slick/slick.css

original: /absolute/path/to/remove_suffix_in_file_names/lib/slick/slick-theme.css?v=B4eGwVoXYEh3pKqquJGr_QHz3FcrGtGRmSS8izz2AAk
replaced: /absolute/path/to/remove_suffix_in_file_names/lib/slick/slick-theme.css

original: /absolute/path/to/remove_suffix_in_file_names/lib/slick/fonts/slick.eot?
replaced: /absolute/path/to/remove_suffix_in_file_names/lib/slick/fonts/slick.eot

original: /absolute/path/to/remove_suffix_in_file_names/lib/bootstrap-datepicker/css/bootstrap-datepicker.standalone.min.css?v=8_PcxkdmqjNGUzE0-tw_RWqI-IAG8-ybXiYBfyHTPbo
replaced: /absolute/path/to/remove_suffix_in_file_names/lib/bootstrap-datepicker/css/bootstrap-datepicker.standalone.min.css

original: /absolute/path/to/remove_suffix_in_file_names/lib/bootstrap-datepicker/css/bootstrap-datepicker.min.css?v=nx7SjIq6Ec0mq8-0Zx5PAgGuYdcYMvpyzuPJCr7q6YI
replaced: /absolute/path/to/remove_suffix_in_file_names/lib/bootstrap-datepicker/css/bootstrap-datepicker.min.css

original: /absolute/path/to/remove_suffix_in_file_names/lib/bootstrap-datepicker/locales/bootstrap-datepicker.ru.min.js?v=iGDUwn2IPSzlnLlVeCe3M4ZIxQxjUoDYdEO6oBZw_Go
replaced: /absolute/path/to/remove_suffix_in_file_names/lib/bootstrap-datepicker/locales/bootstrap-datepicker.ru.min.js

original: /absolute/path/to/remove_suffix_in_file_names/lib/bootstrap-datepicker/js/bootstrap-datepicker.min.js?v=wSn1lWvI6cOig4Bp6aP_UK16VAoHe0KTSyxdfJAvTvw
replaced: /absolute/path/to/remove_suffix_in_file_names/lib/bootstrap-datepicker/js/bootstrap-datepicker.min.js

original: /absolute/path/to/remove_suffix_in_file_names/lib/jquery-validation-unobtrusive/jquery.validate.unobtrusive.min.js?v=9GycpJnliUjJDVDqP0UEu_bsm9U-3dnQUH8-3W10vkY
replaced: /absolute/path/to/remove_suffix_in_file_names/lib/jquery-validation-unobtrusive/jquery.validate.unobtrusive.min.js

original: /absolute/path/to/remove_suffix_in_file_names/lib/fancybox/jquery.fancybox.min.js?v=HALK8qDxYxiWVnb9SyZSZXKNZPuieUogsHFRpOiR_KY
replaced: /absolute/path/to/remove_suffix_in_file_names/lib/fancybox/jquery.fancybox.min.js

original: /absolute/path/to/remove_suffix_in_file_names/lib/unobtrusive-ajax/jquery.unobtrusive-ajax.js?v=54TsJTD6nXoHGcft9-SPH4jgcV_3ayinJaWSmiPWYME
replaced: /absolute/path/to/remove_suffix_in_file_names/lib/unobtrusive-ajax/jquery.unobtrusive-ajax.js

original: /absolute/path/to/remove_suffix_in_file_names/lib/jquery-validation/dist/jquery.validate.min.js?v=6e0N-WJiVKBeTitK1GKSwPi3rbdPpLtuqaiitZjeD2w
replaced: /absolute/path/to/remove_suffix_in_file_names/lib/jquery-validation/dist/jquery.validate.min.js

original: /absolute/path/to/remove_suffix_in_file_names/lib/my-custom-scrollbar/jquery.mCustomScrollbar.css?v=FzDSfCZaTH7qcj5EpRUsb98KPowD0alLR7LhpZSRfqU
replaced: /absolute/path/to/remove_suffix_in_file_names/lib/my-custom-scrollbar/jquery.mCustomScrollbar.css

original: /absolute/path/to/remove_suffix_in_file_names/lib/my-custom-scrollbar/jquery.mCustomScrollbar.js?v=EzmsVDqHl8jBItF1U5XGby3Djd92u8y6A9blx7B7nk4
replaced: /absolute/path/to/remove_suffix_in_file_names/lib/my-custom-scrollbar/jquery.mCustomScrollbar.js

original: /absolute/path/to/remove_suffix_in_file_names/lib/moveto/move-to.min.js?v=KVPBMr_w1-u_gSR6nGm3zdcBP_Q25nR56msdhqv6H1M
replaced: /absolute/path/to/remove_suffix_in_file_names/lib/moveto/move-to.min.js

original: /absolute/path/to/remove_suffix_in_file_names/lib/jquery/dist/jquery.min.js?v=82hEkGrSMJh3quMSG4f7FbngmAPLTDM63H4eNayS4Us
replaced: /absolute/path/to/remove_suffix_in_file_names/lib/jquery/dist/jquery.min.js

original: /absolute/path/to/remove_suffix_in_file_names/lib/select2/css/select2.css?v=f6ld2Ni1kE88xxjBrdMt2It8M6ps4nX0P4rXAnvltWo
replaced: /absolute/path/to/remove_suffix_in_file_names/lib/select2/css/select2.css

original: /absolute/path/to/remove_suffix_in_file_names/lib/select2/js/select2.min.js?v=70QcFVMi3-VGiAVSY1KGFibayMynhoK4aX6BVJErm00
replaced: /absolute/path/to/remove_suffix_in_file_names/lib/select2/js/select2.min.js

original: /absolute/path/to/remove_suffix_in_file_names/lib/select2/js/i18n/ru.js?v=2ND-J51xbuHZNWKJRFeTWZLSA4BOthqob_XNjebdQAQ
replaced: /absolute/path/to/remove_suffix_in_file_names/lib/select2/js/i18n/ru.js
```

<hr style="margin-left: 25%; margin-right: 25%;"></details>

<details><br><summary><b></b>Files names after script:</summary>

```sh
remove_suffix_in_file_names/lib/
├── bootstrap-datepicker/
│   ├── css/
│   │   ├── bootstrap-datepicker.min.css
│   │   └── bootstrap-datepicker.standalone.min.css
│   ├── js/
│   │   └── bootstrap-datepicker.min.js
│   └── locales/
│       └── bootstrap-datepicker.ru.min.js
├── esri-leaflet-geocoder/
│   └── esri-leaflet-geocoder.min.js
├── fancybox/
│   ├── jquery.fancybox.min.css
│   └── jquery.fancybox.min.js
├── jquery/
│   └── dist/
│       └── jquery.min.js
├── jquery-validation/
│   └── dist/
│       └── jquery.validate.min.js
├── jquery-validation-unobtrusive/
│   └── jquery.validate.unobtrusive.min.js
├── leaflet/
│   ├── images/
│   │   ├── layers-2x.png
│   │   ├── layers.png
│   │   └── marker-icon.png
│   ├── leaflet.css
│   └── leaflet.js
├── leaflet-geosearch/
│   ├── esri-leaflet.js
│   └── geosearch.umd.min.js
├── leaflet.markercluster/
│   └── leaflet.markercluster.js
├── moveto/
│   └── move-to.min.js
├── my-custom-scrollbar/
│   ├── jquery.mCustomScrollbar.css
│   └── jquery.mCustomScrollbar.js
├── object-fit-ie/
│   └── object-fit-ie.js
├── select2/
│   ├── css/
│   │   └── select2.css
│   └── js/
│       ├── i18n/
│       └── select2.min.js
├── slick/
│   ├── fonts/
│   │   ├── slick.eot
│   │   ├── slick.svg
│   │   ├── slick.ttf
│   │   └── slick.woff
│   ├── ajax-loader.gif
│   ├── slick.css
│   ├── slick.min.js
│   └── slick-theme.css
└── unobtrusive-ajax/
    └── jquery.unobtrusive-ajax.js

25 directories, 33 files
```

</details>
