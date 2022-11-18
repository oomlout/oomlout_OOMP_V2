SET COMMENT="Quickly Adding Everything"



cd oomlout_OOMP_collections_V2
git pull
git add -A
git commit -m %COMMENT%
git push
cd ..

cd oomlout_OOMP_kicad_V2
git pull
git add -A
git commit -m %COMMENT%
git push
cd ..

cd oomlout_OOMP_modules_V2
git pull
git add -A
git commit -m %COMMENT%
git push
cd ..

cd oomlout_OOMP_partNumbers_V2
git pull
git add -A
git commit -m %COMMENT%
git push
cd ..

cd oomlout_OOMP_social_V2
git pull
git add -A
git commit -m %COMMENT%
git push
cd ..

cd oomlout_OOMP_projects_V2
git pull
git add -A
git commit -m %COMMENT%
git push
cd ..

cd oomlout_OOMP_parts_V2
git pull
git add -A
git commit -m %COMMENT%
git push
cd ..

cd oomlout_OOMP_eda_V2
git pull
git add -A
git commit -m %COMMENT%
git push
cd ..

pause
