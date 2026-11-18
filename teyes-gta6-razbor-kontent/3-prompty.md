# Промты «в стиле GTA» – библиотека и разбор под карусели автосервиса

18.11.2026. Ничего не генерировали – только собрали промты из открытых источников и разобрали. Картинки-результаты взяты из тех же источников (не наши генерации), лежат в `img/`.

## Вывод одной строкой

Узнаваемый «GTA-вид» дают не слова «GTA 6», а техника рисунка: толстый чёрный контур + cel-shading + полуреалистичное лицо + закатный градиент розовый-оранжевый-бирюзовый + постерная композиция (портрет на плоском фоне с силуэтами или сетка панелей). Логотипы, персонажей и слово «official» в промт не пишем.

## Главное (10 строк)

1. Собрано **168 промтов** дословно с 46 страниц на 22 сайтах (+10 негативных промтов, +5 своих шаблонов): ChatGPT / gpt-image / GPT Image 2 (≈105), Flux и SDXL с LoRA (≈33), DALL-E (12), Midjourney (11), Nano Banana / Gemini (4), часть русских «для любого сервиса»; к 16 промтам – картинка-результат из источника.
2. Рабочий промт = 8 частей: задача (перерисовать фото / новая сцена) → кого сохранить → кто и что делает → где → техника рисунка → палитра и свет → композиция и формат → чего не надо.
3. Стиль держат слова: `thick black ink outlines`, `cel-shaded`, `flat saturated color blocks`, `semi-realistic painted face`, `hard shadows`, `halftone grit`, `loading-screen illustration`, `poster cropping`, `low-angle hero shot`.
4. Стиль убивают: `ultra-realistic`, `photograph`, `hyperrealism`, `8K photo`, `Unreal Engine` – на 4 из 16 картинок (№06, 07, 08, 16) вышло обычное фото, рисунка нет.
5. Слова `official`, `Rockstar`, `Grand Theft Auto VI title`, `Add GTA 6 Logo` сразу рисуют чужой логотип и значок R (картинки №12, №13) – для бизнеса это прямое нарушение прав на товарный знак.
6. GTA-стиль по умолчанию тропический (пальмы, Майами); зиму Новосибирска надо прописывать явно и убирать пальмы, иначе модель их вставит. В русских промтах-источниках «не генерируй зимний пейзаж» стоит прямо в антипромте.
7. ChatGPT / Nano Banana – длинный абзац на естественном языке + фото-референс + «сохрани лицо» + «no text, no logos». Midjourney – короткие токены + хвост стиля + `--ar 4:5 --s 250–750 --no text, logo`. Flux / SD – слово-триггер LoRA (`aidmaGTA6`, `gta6style`) с весом 0.5–1.0, CFG ≈3.5.
8. Для автосервиса лучшие заготовки: мастер с ключом на плоском горчичном фоне с силуэтами гаража (№05), сцена в тюнинг-гараже LS Car Meet (P080), портрет у машины на закате (P079), обложка-сетка 3×3 (P065).
9. Тему угона, ограблений, оружия и полиции не брать: для сервиса она бьёт по доверию («угон» у клиента – беда), а оружие режет охват и модерацию. Вместо «heist» – «миссия»: «Миссия: завести в −35».
10. Русский текст и номера машин модели рисуют плохо – заказывать пустую плашку под текст и пустые номера, текст ставить в Figma / Canva потом. 5 своих шаблонов под автосервис – в конце файла.

Что раскрыть: любой раздел ниже; самое полезное для работы – разделы 8–12 (разбор, права, шаблоны).

## Как читать

- Промты – дословно, как в источнике (с опечатками и длинными тире авторов), внутри блоков кода. Комментарии мои – по-русски.
- У каждого: модель, для которой писался (по словам источника), ссылка, картинка-результат, если есть.
- «Модель не указана» – источник дал промт без привязки к нейросети.
- Где в промте реальные персонажи, знаменитости или логотипы – помечено **(анти-пример)**: брать структуру, не содержание.

## Картинки-результаты из источников (16 шт.)

| Файл | К какому промту | Модель | Что видно |
|---|---|---|---|
| `img/prompt-01-lorka-loading-portrait.webp` | P004 | Lorka (модель не названа) | классический «загрузочный экран»: контур, закат, силуэт города |
| `img/prompt-02-lorka-muscle-car.webp` | P006 | Lorka | человек у маслкара, улица с пальмами и вывесками |
| `img/prompt-03-lorka-skyline-cover.webp` | P005 | Lorka | крупный портрет-обложка на закате |
| `img/prompt-04-lorka-mission-passed.webp` | раздел 5, промт не опубликован | Lorka | интерьер магазина под заголовком «Mission passed! Respect +99»; оружие в кадре – для нас не годится |
| `img/prompt-05-civitai-mechanic.webp` | P082 | GTA Style LoRA (Civitai) | **мастер с ключом на плоском горчичном фоне с силуэтами гаража – эталон для сервиса** |
| `img/prompt-06-civitai-supercar.webp` | P084 | Flux + aidmaGTA6 | чёрный суперкар в темноте; стиль пропал из-за `ultra-realistic` |
| `img/prompt-07-civitai-wet-road.webp` | P085 | Flux + aidmaGTA6 | ночная мокрая улица, неон; похоже на фото, а не рисунок |
| `img/prompt-08-civitai-billboard.webp` | P144 | Flux + aidmaGTA6 + aidmaHyperrealism | сатирический билборд; фото-реализм, текст читается |
| `img/prompt-09-dalle-gwagon.webp` | P092 | DALL-E | G-класс на пирсе с колесом обозрения |
| `img/prompt-10-dalle-ford-ranger.webp` | P095 | DALL-E | пикап в пыли на грунтовке |
| `img/prompt-11-mj-motorbike-portrait.webp` | P061 | Midjourney | живописный портрет у мотоцикла на закате – классический MJ-хвост стиля |
| `img/prompt-12-postium-chatgpt-poster.webp` | P014 | ChatGPT Images 2.0 | постер с надписью Grand Theft Auto VI и значком R – **так нельзя для бизнеса** |
| `img/prompt-13-mediaio-neon-hero.webp` | P026 | Media.io (ChatGPT-промт) | неоновый постер, снова логотип GTA VI и значок R |
| `img/prompt-14-youmind-retro-miami.webp` | P116 | GPT Image 2 | ретро-Майами 80-х; лицо вышло похожим на известного актёра, хотя промт просил размыть – риск чужого лица |
| `img/prompt-15-youmind-beach-hud.webp` | P133 | GPT Image 2 | «скриншот игры» с мини-картой и счётчиком денег |
| `img/prompt-16-civitai-car-night.webp` | P089 | Z-Image / SDXL + GTA style LoRA | машина на ночной улице; фото, а не рисунок |

---

## 1. Портрет человека по фото «в стиле GTA» (главный тренд ChatGPT)

### 1.1. Загрузочный экран по фото

**P001. Classic Loading-Screen Portrait** – модель: ChatGPT (GPT-4o / gpt-image) · источник: [Techpresso, 30 prompts](https://academy.techpresso.co/prompts/chatgpt-prompts-gta)
```text
Transform [YOUR PHOTO] into a bold cel-shaded loading-screen illustration in a gritty satirical open-world video-game art style. Keep my face and likeness recognizable but render it with thick black outlines, flat saturated color blocks, hard cartoon shadows, and a slight halftone grit. Frame me as a single confident street character against a sun-bleached urban backdrop with palm trees and a hazy skyline. Poster-style cropping, vivid daytime light, high-contrast comic shading, 4:5 portrait.
```
Совет автора: заменить фон на `a rainy downtown street at night` – более мрачный вариант. Важно: в промте нет слова GTA – только описание техники. Это и есть безопасный приём.

**P002. Action Pose Loading Card** – ChatGPT · [Techpresso](https://academy.techpresso.co/prompts/chatgpt-prompts-gta)
```text
Turn [YOUR PHOTO] into a dynamic loading-screen action card in a gritty cel-shaded open-world art style. Keep my face recognizable but pose me mid-stride looking back over the shoulder with attitude. Thick black outlines, punchy saturated color, hard directional sunlight, dust and motion smears behind me, and a hazy palm-lined boulevard backdrop. Bold satirical poster cropping, comic-grit texture, 4:5 portrait.
```
Совет: добавить `low-angle hero shot`.

**P003. Neon Night Loading Panel** – ChatGPT · [Techpresso](https://academy.techpresso.co/prompts/chatgpt-prompts-gta)
```text
Transform [YOUR PHOTO] into a nighttime loading-screen portrait in a bold cel-shaded street-game style. Keep my likeness, lit by pink and electric-blue neon from storefront signs reflecting on the skin. Thick outlines, flat saturated shadows, gritty halftone texture, and a rain-slicked downtown street with glowing signage and distant skyscrapers behind me. Cinematic satirical urban poster composition, high contrast, 4:5 portrait.
```
Совет: `wet asphalt reflecting the neon`.

**P004. Loading-screen portrait** – модель не названа (генератор Lorka на нескольких моделях) · [Lorka AI](https://www.lorka.ai/knowledge-hub/gta-ai-filter-prompts) · картинка: `img/prompt-01-lorka-loading-portrait.webp`
```text
Turn this photo into a GTA-inspired loading-screen portrait. Preserve the person's facial features and expression. Use a low-angle shot from chest height, dramatic side lighting, and a blurred city skyline background. Bold outlines, cel-shaded coloring, a confident stance, and a cinematic mood.
```
Самый короткий из рабочих – хороший «скелет».

**P005. Skyline hero cover** – Lorka · [Lorka AI](https://www.lorka.ai/knowledge-hub/gta-ai-filter-prompts) · картинка: `img/prompt-03-lorka-skyline-cover.webp`
```text
Close-up cover-style portrait, subject positioned slightly off-center, confident and direct gaze toward camera. Sunset skyline in the background with warm orange and pink light. Bold outlines, cel-shaded coloring, high contrast, GTA-inspired cover art aesthetic. Sharp focus on facial features, cinematic lighting, 1080x1350 vertical format.
```
1080×1350 = формат карусели Инстаграма 4:5.

**P006. Los Santos streets (замок лица)** – Lorka · [Lorka AI](https://www.lorka.ai/knowledge-hub/gta-ai-filter-prompts) · картинка: `img/prompt-02-lorka-muscle-car.webp`
```text
Use the provided reference photo as the highest-priority facial reference. Preserve the individual's facial identity with maximum accuracy. Maintain their exact hairstyle, facial features, eyebrows, eyes, nose, lips, jawline, skin texture, facial proportions, and all unique facial characteristics. Do not generate a generic GTA character. Rafael Franco must remain recognizable while being illustrated in premium Grand Theft Auto promotional artwork style. Official GTA-inspired key art aesthetic, ultra detailed, AAA quality, Rockstar Games promotional artwork quality, cinematic composition, dramatic lighting, highly detailed environment, professional illustration, sharp focus, 1080x1350 vertical format.
```
Полезна первая половина – «замок лица» для фото мастера. Вторая половина (`Official`, `Rockstar Games`) – рискованная, см. раздел 10.

**P007. Neon alley chase** – Lorka · [Lorka AI](https://www.lorka.ai/knowledge-hub/gta-ai-filter-prompts)
```text
Use the provided reference photo as the highest-priority facial reference. The individual sprinting through a narrow urban alley in Los Santos at night. Camera positioned behind and slightly below him creating a dynamic chase perspective. Neon signs reflecting on wet pavement. Graffiti-covered walls. Police lights visible in the distance. Motion blur emphasizing movement. Dramatic shadows. High energy GTA action artwork. Rockstar promotional illustration quality. Ultra detailed environment. AAA game artwork. 1080x1350.
```

**P008. Fence-jump pursuit scene** – Lorka · [Lorka AI](https://www.lorka.ai/knowledge-hub/gta-ai-filter-prompts)
```text
Use the provided reference photo as the highest-priority facial reference. The individual mid-air while jumping over a chain-link fence during a pursuit. Camera positioned below the fence looking upward. Dynamic action pose. Los Santos skyline in the background. Sunset sky with orange and purple tones. Motion blur on the environment while the individual remains sharp. Cinematic action moment. Rockstar Games key art style. GTA promotional artwork quality. Ultra detailed illustration. AAA quality. 1080x1350.
```

**P009. Helicopter over city** – Lorka · [Lorka AI](https://www.lorka.ai/knowledge-hub/gta-ai-filter-prompts)
```text
Subject piloting a helicopter high above a sprawling city skyline during sunset. Camera positioned outside the aircraft near the cockpit, slightly below and in front, creating an epic cinematic perspective. Subject clearly visible through the cockpit glass, one hand on the controls, focused expression. City skyline, highways, and palm trees below, illuminated by orange and purple sky. Rotor blades with subtle motion blur. GTA-inspired promotional artwork aesthetic, ultra-detailed, cinematic lighting, 1080x1350 vertical composition.
```

**P010. BMX at sunset** – Lorka · [Lorka AI](https://www.lorka.ai/knowledge-hub/gta-ai-filter-prompts)
```text
Subject riding a BMX bike along a beachfront boardwalk at sunset, mid-pedal with a relaxed, confident posture. Camera positioned at a low side angle to emphasize motion and speed. Palm trees, ocean, and glowing sky in the background, warm golden-hour lighting. Bold outlines, vibrant colors, GTA-inspired illustration style, dynamic composition, sharp focus on the subject.
```

**P011. Your Photo as Loading-Screen Art (перерисовать, ничего не добавляя)** – image-to-image (ChatGPT, Gemini, Media.io) · [Media.io, GTA 6 loading screen](https://www.media.io/ai/explore/zone/gta-6-loading-screen-ai-generator)
```text
Image Prompt: Your Photo as Loading-Screen Art. Transform the uploaded photo into a fan-made GTA VI-inspired loading-screen illustration. Preserve the person’s recognizable facial features, hairstyle, skin tone, expression, outfit and pose. Keep the original camera angle, framing, number of people and arrangement of background objects. Redraw the entire image with clean black ink contours, semi-realistic painted faces, cel-shaded color blocks and crisp directional shadows. Apply a warm coral, pink and turquoise color grade while keeping the original scene recognizable. Give the subject and background a consistent illustrated finish. Create one still image in the original aspect ratio. Do not add people, cars or objects that are absent from the photo. No text, logos, watermark or game interface.
```
**Лучший образец для наших реальных фото из бокса**: перерисовать кадр, ничего не выдумывая, без логотипов.

**P012. Two People, One Poster (пара)** – image-to-image · [Media.io](https://www.media.io/ai/explore/zone/gta-6-loading-screen-ai-generator)
```text
Image Prompt: Two People, One Poster. Transform the two people in the uploaded couple photo into a GTA-style couple loading-screen portrait. Preserve each person’s distinct face, hairstyle, skin tone, build and outfit. Keep the same left-to-right order as in the reference without mixing their identities. Show them standing close together in relaxed, confident poses on a palm-lined waterfront at sunset. Place a parked convertible behind them, with pastel coastal buildings and a pink-purple sky in the distance. Keep both faces visible and give each person equal visual importance. Use clean black ink contours, semi-realistic painted faces, cel-shaded color blocks and warm directional shadows. Create one unified vertical 9:16 illustration with exactly two people, natural anatomy and clearly separated silhouettes. No text, logos, watermark or game interface.
```
Годится для «мастер + клиент у машины».

**P013. Your Pet as the Protagonist** – image-to-image · [Media.io](https://www.media.io/ai/explore/zone/gta-6-loading-screen-ai-generator)
```text
Image Prompt: Your Pet as the Protagonist. Turn the pet in the uploaded photo into the sole main character of a GTA-inspired pet loading-screen illustration. Preserve its species, facial features, coat colors, fur markings, ear shape, eye color and natural body proportions. Keep any collar or accessory already present. Show the pet sitting confidently on a Miami-inspired beachfront promenade, with palm silhouettes, pastel art-deco buildings, a distant parked sports car and a coral-pink sunset. Keep its face unobstructed and its silhouette clearly separated from the background. Illustrate the entire scene with bold black contours, painted fur details, cel-shaded colors and crisp sunset shadows. Vertical 9:16 poster composition. Keep natural animal anatomy and paws; do not turn the pet into a human or add clothing. No other animals, people, text, logos or watermark.
```
Идея для сервиса: «кот мастера на капоте» – живой контент.

### 1.2. Постер-портрет по фото

**P014. Игровой постер (Postium, промт 1)** – проверен автором в ChatGPT Images 2.0, Nano Banana 2, Qwen Image 2.0 · [Postium, 16.11.2026](https://postium.ru/promt-dlya-foto-v-stile-gta-6/) · картинка: `img/prompt-12-postium-chatgpt-poster.webp`
```text
Create a highly detailed 8K portrait poster inspired by the iconic visual style of the modern Grand Theft Auto VI promotional artwork aesthetic, featuring a cinematic urban atmosphere with bold composition, vibrant lighting, layered graphic elements, and stylish contemporary street-luxury fashion energy. The overall design must strongly capture the signature mood of GTA VI posters, including dynamic neon color grading, tropical-modern city vibes, dramatic shadows, glossy highlights, stylized textures, decorative ornaments, graphic overlays, urban symbols, luxury lifestyle accents, and immersive environmental storytelling. Add premium poster decorations such as abstract shapes, graffiti-inspired accents, subtle retro-modern textures, luxury vehicle silhouettes, nightlife elements, palm tree shadows, street sign details, glowing reflections, and layered visual effects that enrich the composition without making it feel overcrowded. Include a large cinematic title text “Grand Theft Auto VI” prominently on the poster using typography inspired by official AAA video game promotional posters, with the full version of “GTA” clearly written as “Grand Theft Auto.” The typography should feel bold, luxurious, modern, and integrated naturally into the poster design, supported by additional smaller decorative texts, symbols, labels, and graphic UI-style elements to strengthen the authentic game-poster atmosphere. The subject must not replicate the exact pose from the reference photo. Create a completely fresh and more visually engaging pose with stronger body language, natural movement, and expressive emotion. The expression should feel alive, charismatic, confident, and cinematic rather than stiff, awkward, or flat. The pose must resemble the elegance and attitude of an international fashion model, combining stylish confidence with relaxed realism. Avoid static standing poses. Instead, use dynamic posture, subtle movement, fashionable gestures, asymmetrical body positioning, realistic interaction with the environment, and strong eye expression to create a premium editorial look. The outfit should feature trendy modern casual fashion with a luxurious streetwear influence. The clothing must feel fashionable, youthful, and visually rich, avoiding plain or monotonous styling. Combine varied colors, layered clothing pieces, modern fabric textures, unique motifs, stylish accessories, and contemporary fashion details that complement the GTA VI-inspired atmosphere. The styling should feel premium, photogenic, and believable, similar to high-end editorial fashion mixed with modern open-world video game aesthetics. Use cinematic lighting with realistic skin texture, detailed fabric rendering, atmospheric reflections, depth-rich environment composition, balanced contrast, and ultra-sharp visual clarity. The poster should feel like an official next-generation AAA game promotional artwork with highly polished rendering quality, immersive visual storytelling, and professional graphic design execution. Ultra-detailed, highly aesthetic, cinematic composition, realistic proportions, premium poster layout, vibrant modern color palette, visually powerful, and rendered in ultra high-definition 8K quality.
```
**(анти-пример для бизнеса)**: просит название игры – на картинке №12 вышел логотип GTA VI и значок R. Для личной аватарки – популярный вариант, для рекламы сервиса – нельзя.

**P015. GTA Style Character Transformation (по позе-референсу)** – GPT Image 2 · [YouMind](https://youmind.com/prompts/gta-style-identity-transformation-33569)
```text
Use my photo as the main identity reference. Use the target image I'm going to attach as reference for pose, composition, framing, lighting, setting, color palette, and visual style. Replace the character in the target image with the person from my photo, keeping my identity recognizable: face, hair, beard, skin tone, physical build, serious expression, and main facial features. Keep exactly the pose, body posture, arm and hand position, framing, composition, perspective, lighting, and setting from the target image. Don't alter the environment, colors, or original atmosphere except for the minimum needed to naturally integrate the new character. Reconstruct the full character, don't just do a simple face swap. Adapt my face and body to the pose of the target image, maintaining realistic anatomy, natural proportions, and coherence between head, neck, shoulders, arms, and hands. Apply a visual style clearly inspired by GTA cover art: stylized-realism character illustration, defined outlines, skin and clothing with a polished painterly finish, high contrast, cinematic lighting, saturated but controlled colors, luxury-meets-street urban aesthetic. Avoid making it look like a generic illustration or a photo filter. Keep the outfit from my photo: oversized white t-shirt, black watch, and bracelet/chain on the wrist. You can subtly improve the texture, drape, and finish of the clothing to make it look more premium, but without changing the main outfit. Replace any bag or handheld object from the target image with a premium black urban-style backpack, naturally integrated into the pose and scene. Add GTA 6 Logo Do not include: camera equipment, gimbal, audiovisual gear, real logos, text, trademarks, weapons, facial deformities, poorly constructed hands, excessive muscle mass, cartoonish appearance, or costume-like look.
```
Ценный приём – два фото: «лицо» + «поза/композиция». Противоречие внутри: `Add GTA 6 Logo` и тут же `Do not include: real logos` – так писать не надо.

**P016. GTA6 template (Magic Hour)** – gpt-image-2 · [Magic Hour](https://magichour.ai/templates/details/cmqxha4gp01slgh0z1unhruv3-gta6)
```text
This style redraws you as the star of a GTA 6 / Vice City cover art — a bold cel-shaded illustration with clean linework, vibrant colors and a neon Miami sunset. Your real face, gender, hairstyle, skin tone and body are preserved, just reimagined in glossy game-poster style against a rooftop pool backdrop with palm trees and glowing signs. Then the poster comes alive: you lower your hand past your face and blow a gentle kiss to the camera while a warm breeze moves your hair. A chill, cinematic motion-poster moment with a synthwave Vice City vibe.
```
Вторая половина – для оживления в видео.

**P017. YouCam, 3D-рендер** – модель не указана (YouCam AI Pro, image-to-image) · [Perfect Corp](https://www.perfectcorp.com/consumer/blog/generative-AI/gta-filter)
```text
Please refer to the photographic materials in Figure 1 to create a high-quality surreal 3D rendering in the GTA style; for the image of this young woman, do not alter the original facial contours; the work must feature the GTA aesthetic style and illustrative style.9:16Original.Original.
```

**P018. YouCam, короткий** – YouCam AI Pro · [Perfect Corp](https://www.perfectcorp.com/consumer/blog/generative-AI/gta-filter)
```text
Create a GTA loading screen–style illustration with bold outlines, cinematic lighting, and vibrant colors.
```

**P019–P020. Двухшаговый метод «сначала стиль, потом фото»** – ChatGPT (GPT-4o), Gemini, Grok, Copilot · [Analytics Insight](https://www.analyticsinsight.net/gaming/how-to-turn-your-images-into-gta-6-art-using-ai-chatgpt-gemini-and-more)
```text
Learn the visual style of these GTA 6 images. Focus on colors, shading, outlines, background elements, and character design.
```
```text
Convert this photo into GTA 6 style based on the previous references.
```
Работает, но требует загрузить официальные арты Rockstar как референс – для бизнеса не советую; заменить на свои референсы, сгенерированные без логотипов.

**P021. Pincel, «проверенный»** – Pincel AI (image-to-image) · [Pincel](https://blog.pincel.app/gta-style/)
```text
SUBJECT, GTA 5 style illustration, cartoon, colorful drawing, vivid colors
```

**P022. GTA V как кадр движка (не рисунок)** – Nano Banana Pro / Nano Banana · [Telegram «Дизайнерская бытовуха»](https://t.me/s/disignbit/625)
```text
PRIMARY_DIRECTIVE: Perform a FORCED GAME-ENGINE RE-RENDER while keeping the scene spatially locked. The input image is a fixed spatial blueprint for layout only and is NOT a valid final render. The current photographic lighting and materials are INCORRECT and MUST be replaced. Preserve object count, object position, scale, perspective, camera angle and framing exactly, but fully replace materials, shaders, lighting and surface response. Convert the image into an authentic GTA V / GTA Online in-engine render with clearly recognizable Rockstar RAGE engine look. Lighting must follow GTA V in-game tone mapping and color filtering, with compressed dynamic range, slightly overexposed highlights, reduced midtone detail and a subtle global color filter applied across the entire frame. The scene must feel filtered through the GTA V engine, not neutrally lit. Add subtle atmospheric haze typical of GTA V daytime scenes. Skin must use GTA V character skin shader: smooth, waxy, artificial-looking, with flat color zones, no visible pores, no realistic skin texture and simple non-physical specular highlights. Faces must clearly read as game characters, not real people. Clothing must use GTA V in-game material shaders with simplified texture detail and artificial surface response. Shadows must look like real-time engine shadows with slight noise and imperfect softness, not cinematic or physically accurate. Texture resolution must be reduced to true game-level detail with slight softness and compression artifacts. Geometry must show subtle game-like angularity and non-perfect smoothing. The background and environment must stay exactly the same in layout but appear fully re-rendered through the GTA V engine with the same global lighting filter applied. The image must clearly look like a paused GTA V gameplay frame, not a photo and not an illustration. Add the official GTA V logo as a flat 2D overlay in a corner like a Rockstar promo screenshot. If the lighting looks neutral, photographic or physically accurate instead of filtered and engine-driven, the generation has failed.
```
Другой жанр – не арт, а «скриншот игры». Приём «если выглядит как фото – генерация провалена» полезен. Последнюю фразу про логотип – убрать.

**P023. Vice City как движок 2002 года** – Nano Banana Pro / Nano Banana · [Telegram «Дизайнерская бытовуха»](https://t.me/s/disignbit/625)
```text
CRITICAL: ENGINE-ACCURATE STYLE TRANSFER ONLY. This is NOT artwork, NOT illustration, NOT fan art, NOT remake, NOT cinematic render. Use the attached photo strictly as layout and composition reference. Do not change pose, framing, camera angle or object positions. The goal is to DOWNGRADE the image into an authentic early-2000s real-time game render exactly matching the ORIGINAL GTA Vice City engine limitations. Replace all photographic detail with low-resolution in-game textures, flat color maps and visible low-poly geometry. Faces must look clearly polygonal with angular structure, minimal texture detail, flat shading and no realistic skin features. Clothing must look like original Vice City NPC clothing with simple color blocks, blurry low-res textures, no fabric detail and no material realism. All surfaces must look artificially game-rendered, never painterly, never illustrative. Lighting must be crude real-time engine lighting with hard shadows, no ambient bounce, no global illumination, no depth of field and no cinematic contrast. Colors must be slightly washed with pastel pink, cyan and warm sunset tones exactly like Vice City gameplay. The image must look like a raw paused gameplay or cutscene frame captured directly from the 2002 game engine, with visible technical limitations. Add the official GTA Vice City logo as a flat 2D overlay in a corner like an old Rockstar promo screenshot. If the result looks like art, illustration, stylized painting or modern remake, the generation is incorrect.
```
Смешной формат «наш бокс в графике 2002 года» – хорош для юмора в карусели (без логотипа).

**P024. Шаг 1 Media.io** – ChatGPT, Gemini, Media.io · [Media.io, poster prompts](https://www.media.io/image-effects/chatgpt-gta-style-poster-prompts.html)
```text
Turn this photo into a cinematic GTA 6 style poster with neon Miami sunset lighting, palm trees, luxury sports cars, dramatic shadows, bold Rockstar-inspired composition, vibrant pink and orange color grading, ultra detailed game cover artwork
```

**P025. Neon Criminal Hero Poster** – ChatGPT · [Media.io](https://www.media.io/image-effects/chatgpt-gta-style-poster-prompts.html) · картинка: `img/prompt-13-mediaio-neon-hero.webp`
```text
Create an ultra cinematic GTA 6 style poster of a confident street character standing in a neon-lit Miami alley at sunset. Low-angle camera shot with tropical palm trees, glowing pink and orange lighting, luxury sports car positioned behind the subject. Feature dramatic shadows, Rockstar-inspired promotional artwork aesthetic, bold graphic composition, hyper realistic textures with atmospheric smoke, and official game cover design language.
```
`official game cover design language` → на картинке логотип и значок рейтинга ESRB. Так работает слово «official».

**P026. Vice City Nightlife Poster** – ChatGPT · [Media.io](https://www.media.io/image-effects/chatgpt-gta-style-poster-prompts.html)
```text
Transform the portrait into a GTA VI nightlife poster surrounded by vibrant neon signs and rain reflections. Incorporate luxury nightclubs, glowing streets, cinematic blue and magenta lighting with dramatic depth of field. Showcase stylish streetwear fashion on the subject with intense expression, cinematic realism, and official Rockstar promotional styling to capture the authentic Vice City nightlife essence.
```
(Номер картинки №13 на странице Media.io стоит рядом с P025–P026, точную привязку источник не подписал.)

**P027. GTA 6 Female Protagonist Style** – ChatGPT · [Media.io](https://www.media.io/image-effects/chatgpt-gta-style-poster-prompts.html)
```text
Create a GTA 6 inspired female protagonist poster exuding powerful attitude against a tropical Miami background. Feature sunset sky gradients with cinematic orange and pink glow, luxury jewelry accents, and dramatic shadows. Include palm trees and sports car reflections in the composition, rendered in modern Rockstar game art style with bold cinematic composition and commanding presence.
```

**P028. Low Angle Action Hero Cover** – ChatGPT · [Media.io](https://www.media.io/image-effects/chatgpt-gta-style-poster-prompts.html)
```text
Generate a cinematic GTA 6 action poster from a dramatic low-angle perspective showing the character standing powerfully in the middle of a neon urban street. Include glowing police lights, motion blur effects, luxury vehicles surrounding the scene, atmospheric smoke, high contrast lighting, and ultra detailed Rockstar-inspired game cover art that captures intense action energy.
```

**P029. Instagram Main Character Energy** – ChatGPT · [Media.io](https://www.media.io/image-effects/chatgpt-gta-style-poster-prompts.html)
```text
Turn this selfie into a GTA 6 style cinematic portrait radiating strong main-character energy. Feature neon Miami nightlife background with dramatic shadows, luxury fashion styling on the subject, glowing city reflections, cinematic depth of field, and Rockstar-inspired promotional composition. Apply vibrant orange and magenta color grading to create Instagram-worthy visual impact.
```

**P030. Luxury Lifestyle GTA Poster** – ChatGPT · [Media.io](https://www.media.io/image-effects/chatgpt-gta-style-poster-prompts.html)
```text
Create a luxury GTA VI style portrait featuring designer streetwear and gold accessories under tropical sunset lighting. Showcase exotic sports cars, cinematic reflections, high-end nightclub atmosphere, and bold game artwork composition. Emphasize realistic skin textures and ultra detailed AI poster aesthetic that conveys wealth, status, and aspirational lifestyle through premium visual elements.
```

**P031. Rainy Neon Street Edit** – ChatGPT · [Media.io](https://www.media.io/image-effects/chatgpt-gta-style-poster-prompts.html)
```text
Generate a GTA 6 rainy street portrait with wet asphalt reflections and cinematic neon signs creating dramatic backlighting. Establish moody atmosphere with realistic rain particles, Miami-inspired nightlife environment, and cinematic realism throughout the composition. Capture Rockstar promotional poster energy through atmospheric weathering and urban grit that enhances the street-level authenticity.
```

**P032. Streetwear Editorial GTA Art** – ChatGPT · [Media.io](https://www.media.io/image-effects/chatgpt-gta-style-poster-prompts.html)
```text
Create a GTA 6 inspired streetwear editorial poster showcasing futuristic urban fashion with cinematic neon shadows and reflective textures. Feature glowing sunset sky backdrop, sports car background elements, and Rockstar-style character illustration throughout. Employ dramatic cinematic framing that elevates streetwear aesthetics to high-fashion editorial standards while maintaining authentic game art DNA.
```

**Доп. (не входит в счёт). Relight Image (ночная вспышка)** – Media.io (вшит в ссылку «Start Free») · [Media.io](https://www.media.io/image-effects/chatgpt-gta-style-poster-prompts.html)
```text
Relight image. Background: Deep and muted, darker tone at the top, grainy.
```
Источник показал только начало, дальше – пересказ: ночная вспышка, контровой свет, мягкая заливка спереди, высокий контраст. Полного текста нет.

### 1.3. Архетипы и компании (Techpresso, ChatGPT)

**P033. Slick Mobster** – ChatGPT · [Techpresso](https://academy.techpresso.co/prompts/chatgpt-prompts-gta)
```text
Reimagine [YOUR PHOTO] as a slick mobster character in a bold cel-shaded satirical street-game style. Keep my face recognizable, dressed in a sharp pinstripe suit with a loosened tie, posed with cool menace. Thick ink outlines, flat saturated tones, dramatic noir shadows, and a dim back-alley or smoky lounge backdrop. Cinematic low-key lighting, gritty comic texture, satirical poster composition, 4:5 portrait.
```

**P034. Biker Gang Leader** – ChatGPT · [Techpresso](https://academy.techpresso.co/prompts/chatgpt-prompts-gta)
```text
Turn [YOUR PHOTO] into a biker-gang-leader character in a gritty cel-shaded video-game style. Keep my likeness recognizable, wearing a worn leather vest with patches and dark shades, straddling a chopper motorcycle. Thick black outlines, flat saturated color, dusty hard sunlight, and a wide desert highway with distant mesas behind me. Rugged satirical poster cropping, high contrast, 4:5 portrait.
```

**P035. Corrupt Cop** – ChatGPT · [Techpresso](https://academy.techpresso.co/prompts/chatgpt-prompts-gta)
```text
Transform [YOUR PHOTO] into a satirical corrupt-cop character in a bold cel-shaded street-game style. Keep my face recognizable in a rumpled uniform with mirrored aviators and a smug grin. Thick outlines, flat saturated tones, harsh midday shadows, and a city precinct or patrol-car backdrop with red-and-blue light glow. Gritty satirical poster composition, high contrast, comic halftone grit, 4:5 portrait.
```

**P036. Beach Hustler** – ChatGPT · [Techpresso](https://academy.techpresso.co/prompts/chatgpt-prompts-gta)
```text
Reimagine [YOUR PHOTO] as a flashy beach-hustler character in a saturated cel-shaded satirical style. Keep my likeness recognizable, wearing an open loud-print shirt, gold chains, and sunglasses, posed cocky on a sunny boardwalk. Thick ink outlines, flat vivid color, hard tropical sunlight, and palm trees with rollerbladers behind me. Bold comic shading, satirical urban poster cropping, 4:5 portrait.
```

**P037. Partners-in-Crime Duo** – ChatGPT · [Techpresso](https://academy.techpresso.co/prompts/chatgpt-prompts-gta)
```text
Transform [YOUR PHOTO WITH TWO PEOPLE] into a cel-shaded partners-in-crime duo in a gritty satirical street-game style. Keep both faces and likenesses recognizable, posed back-to-back with confident smirks. Thick black outlines, flat saturated color, hard shadows, and a hazy city boulevard with palm trees behind. Coordinated poster cropping like a game cover, comic-grit texture, high contrast, 4:5 portrait.
```

**P038. Three-Up Crew Lineup** – ChatGPT · [Techpresso](https://academy.techpresso.co/prompts/chatgpt-prompts-gta)
```text
Reimagine [YOUR GROUP PHOTO] as a cel-shaded crew lineup in a bold satirical street-game style. Keep each face recognizable, arranged shoulder-to-shoulder in a confident low-angle hero shot, each person in a distinct streetwear look. Thick ink outlines, flat saturated color, dramatic shadows, and a gritty downtown skyline at dusk behind the group. Game-cover poster composition, high contrast, 16:9 landscape.
```
Под «команда сервиса» – готовая структура; совет автора: назвать число людей, держать 3–4.

**P039. Heist-Squad Poster** – ChatGPT · [Techpresso](https://academy.techpresso.co/prompts/chatgpt-prompts-gta)
```text
Turn [YOUR GROUP PHOTO] into a heist-squad poster in a gritty cel-shaded satirical style. Keep each face recognizable, give each person a role-coded look (driver, hacker, muscle, lookout), posed in a dramatic spread. Thick outlines, flat saturated tones, hard noir shadows, and a vault or city-bank backdrop. Bold game-cover composition with a heavy title bar, comic grit, high contrast, 16:9 landscape.
```
Для сервиса переделать роли: «диагност, электрик, установщик, приёмщик» – и без сейфа.

**P040. Beach Crew Hangout** – ChatGPT · [Techpresso](https://academy.techpresso.co/prompts/chatgpt-prompts-gta)
```text
Reimagine [YOUR GROUP PHOTO] as a beach crew in a bold cel-shaded satirical street-game style. Keep each face recognizable, the group lounging on a sunny boardwalk in loud-print shirts and shades, jet skis and palms behind them. Thick ink outlines, flat saturated tropical color, hard sunlight, and bright sandy tones. Relaxed satirical poster composition, comic grit, high contrast, 16:9 landscape.
```

**P041. Retro 16-Bit Sprite Hero** – ChatGPT · [Techpresso](https://academy.techpresso.co/prompts/chatgpt-prompts-gta)
```text
Transform [YOUR PHOTO] into a retro 16-bit pixel-art game character in a gritty urban-arcade style. Keep my likeness recognizable but reduce it to chunky pixel clusters with a limited saturated palette, bold dithering, and a hard black outline. Pose me as a side-scroller street hero against a pixelated city block with neon signage. Clean sprite-sheet framing, crisp retro arcade aesthetic, 1:1 square.
```

**P042. Gritty Comic Noir Panel** – ChatGPT · [Techpresso](https://academy.techpresso.co/prompts/chatgpt-prompts-gta)
```text
Reimagine [YOUR PHOTO] as a gritty noir comic-book panel in a hard cel-shaded crime-story style. Keep my face recognizable with a tense expression, rendered in heavy black ink, high-contrast spot blacks, and a limited muted palette with one accent color. Add halftone shading, a rain-streaked window, and a narrow caption box at the top. Dramatic graphic-novel composition, moody and cinematic, 2:3 portrait.
```
Совет автора: текст подписи писать в кавычках `'reads ONE LAST JOB'`.

**P043. Stylized 3D Render Cover** – ChatGPT · [Techpresso](https://academy.techpresso.co/prompts/chatgpt-prompts-gta)
```text
Turn [YOUR PHOTO] into a stylized 3D game-render character in a modern open-world cinematic style. Keep my likeness recognizable with semi-realistic proportions, but render with smooth subsurface skin, soft global illumination, and a slightly exaggerated heroic vibe. Pose me confidently against a softly blurred dusk-lit city street. Clean render-trailer composition, cinematic depth of field, high quality, 4:5 portrait.
```

### 1.4. Портреты по частям серии (русские промты, Directline)

Все – «для любого сервиса с фото» (ChatGPT, Nano Banana, Midjourney и др.) · [Directline, 20 промптов](https://www.directline.pro/connect/p/prompt-dlya-foto-v-stile-gta/). Антипромпт автор ставит последней фразой «Не генерируй: …».

**P044. Молчаливый антигерой (GTA III)**
```text
Воспроизведи внешность человека с загруженного фото, сохрани узнаваемые черты лица. Стилизуй под загрузочный экран GTA III. Рисованная иллюстрация с жесткими черными контурами и ячеистой штриховкой (cel-shading). Приглушенная палитра: серый, грязно-синий, бордовый. На фоне — мрачные многоэтажки Либерти-Сити, мост, дождливое небо. Если мужчина — темная кожаная куртка и карго-штаны; если женщина — черный бомбер и темные джинсы. Выражение лица сосредоточенное и угрожающее. Стиль ранних загрузочных экранов Rockstar: слегка угловатые пропорции, высокий контраст. Не генерируй: яркие цвета, улыбку, неоновое освещение, фотореалистичную текстуру кожи, деформацию лица, лишние пальцы.
```

**P045. Неоновая ночь (GTA Vice City)**
```text
Воспроизведи внешность и лицо человека с загруженного фото. Стилизуй под арт GTA Vice City. Яркая иллюстрация в духе загрузочных экранов: розово-фиолетовый закат, пальмы, неоновые вывески, отель Ocean View на заднем плане. Палитра — розовый, бирюзовый, фиолетовый, золотой. Если мужчина — гавайская рубашка с тропическим принтом, белые брюки, золотая цепь; если женщина — открытый топ, мини-юбка, крупные солнцезащитные очки в стиле 80-х. У ног — спорткар Infernus (белый). Рисованный стиль с четкими контурами, cel-shading, атмосфера роскоши и синтвейва. Не генерируй: зимний пейзаж, темную мрачную палитру, реалистичные фототекстуры, размытие, искажение лица, лишние конечности.
```
Обратите внимание: «Не генерируй: зимний пейзаж» – стиль по умолчанию против зимы.

**P046. Грув-стрит навсегда (GTA San Andreas)**
```text
Воспроизведи внешность и лицо человека с загруженного фото. Стилизуй под загрузочный экран GTA San Andreas. Рисованная иллюстрация с жесткими черными контурами, ячеистая штриховка, теплая палитра: золотисто-оранжевый закат, зеленые акценты банды Грув-стрит. На заднем плане — одноэтажные дома района Grove Street, граффити на стенах, припаркованный лоурайдер. Если мужчина — зеленая бандана, белая майка-«алкоголичка», мешковатые джинсы, кеды; если женщина — зеленый кроп-топ, бандана, высокие джинсы, массивные кольца. Поза дерзкая, взгляд в камеру. Стиль: Rockstar art, 2004 год, хип-хоп-эстетика Западного побережья. Не генерируй: неоновые цвета, фотореализм, зимний пейзаж, размытие, деформацию лица, лишние пальцы.
```

**P047. Американская мечта (GTA IV) – холодная палитра, ближе всего к нашей зиме**
```text
Воспроизведи лицо и внешность человека с загруженного фото. Стилизуй под арт GTA IV. Рисованная иллюстрация с высокой детализацией, мягкий cel-shading с реалистичными пропорциями. Палитра холодная: серо-голубой, болотный, тусклый желтый. На заднем плане — мост, напоминающий Бруклинский, небоскребы в дымке, желтые такси. Если мужчина — потертая кожаная куртка, темный свитер, джинсы; если женщина — короткая куртка-косуха, серый шарф, ботинки. Выражение лица суровое и усталое. Стиль: кинематографичный нуар Rockstar, 2008 год. Не генерируй: яркие тропические цвета, улыбку, солнечную погоду, пиксельную графику, деформацию лица, лишние пальцы.
```

**P048. Новый Вайс-Сити (GTA VI – день)**
```text
Воспроизведи внешность человека с загруженного фото. Стилизуй под арт GTA VI. Современный Вайс-Сити: яркий солнечный день, пляж, ар-деко здания Оушен-Драйв, пальмы, голубая вода. Рисованная иллюстрация в стиле Rockstar нового поколения: плавные контуры, высокая детализация, реалистичные пропорции, яркая насыщенная палитра. Если мужчина — расстегнутая льняная рубашка, шорты, тату-рукав, кепка; если женщина — бикини-топ, джинсовые шорты, крупные серьги, татуировка. Поза уверенная, взгляд дерзкий, на фоне — припаркованный кабриолет. Палитра: бирюзовый, коралловый, белый, золотистый. Не генерируй: мрачную палитру, зимний пейзаж, пиксельную графику, ретростиль, деформацию лица, лишние пальцы.
```

**P049. Леонида ночью (GTA VI – ночь у машины)**
```text
Воспроизведи лицо и внешность человека с загруженного фото. Стилизуй под арт GTA VI, ночная сцена в штате Леонида. Заболоченная обочина шоссе, вдалеке — светящиеся огни Вайс-Сити, неоновая вывеска придорожного бара, темное южное небо со звездами. Рисованная иллюстрация Rockstar с плавными контурами и кинематографичным освещением. Если мужчина — расстегнутая рубашка с коротким рукавом, джинсы, цепь; если женщина — обтягивающий топ, юбка, браслеты. Человек стоит у капота автомобиля, подсвеченного фарами. Палитра: глубокий синий, неоново-розовый, теплый оранжевый. Не генерируй: дневной свет, снег, пиксельную графику, мрачный серый стиль GTA IV, деформацию лица, лишние конечности.
```

### 1.5. Midjourney и DALL-E: портреты без фото

**P050. Undertaker WWE** – Midjourney · [The Prompt Index, GTA](https://www.thepromptindex.com/image-database.php?style=GTA) **(анти-пример: реальный человек)**
```text
the man Undertaker of wwe walking through Los Angeles with no hat and big beard in the style of a grand theft auto, loading screens ,GTA style artwork highly detailed, celshading, digital painting style, dramatic composition, 21st century comic book cover, studio lighting
```
Отсюда «классический MJ-хвост» стиля – повторяется во всех MJ-промтах этой подборки.

**P051. Female Portrait 1** – Midjourney · [The Prompt Index](https://www.thepromptindex.com/image-database.php?style=GTA)
```text
African American female young woman with long straight black hair, blue eyes, heavily made up with full red lips, has many tattoos and a faint on her left arm and dress quite tight in the style of a grand theft auto, loading screens ,GTA style artwork highly detailed, celshading, digital painting style, dramatic composition, 21st century comic book cover, studio lighting
```

**P052. Female Portrait 2** – Midjourney · [The Prompt Index](https://www.thepromptindex.com/image-database.php?style=GTA)
```text
a 26 year old young woman, white hair, blue eyes, freckles, full lips. Both arms tattooed. Black cap backwards, short t-shirt and torn pants, nike sneakers in the style of a grand theft auto, loading screens ,GTA style artwork highly detailed, celshading, digital painting style, dramatic composition, 21st century comic book cover, studio lighting
```

**P053. Character Portrait** – DALL-E · [The Prompt Index](https://www.thepromptindex.com/image-database.php?style=GTA)
```text
Character portrait in the style of GTA 5 loading screen art, gang member.
```

**P054–P057. Футболист в GTA-стиле (4 варианта)** – Midjourney v5.3, промты написаны ChatGPT по шаблону · [WildVis / WildChat 1597614](https://wildvisualizer.com/conversation/wildchat/1597614)
```text
/imagine prompt: In a GTA style, a Brazilian football player with a shaved head, wearing a bright yellow jersey, jumps in the air with his arms raised in celebration of a goal. The player's face is filled with excitement and happiness, with his mouth wide open and his eyes closed in sheer joy. The artwork incorporates elements of graphic design and inspired illustrations, showcasing the player in a realistic manner with lifelike accuracy. The background features a flat aquamarine color and is adorned with dark orange accents, creating a vibrant and energetic atmosphere. The overall mood of the artwork is joyful and exuberant, reflecting the moment of triumph on the football field. --ar 16:9 --v 5.3
```
```text
/imagine prompt: Immersed in the dynamic action of a football match, a renowned Brazilian football player stands tall in a crowded stadium after successfully scoring a goal. The player's jersey, in bright yellow, displays his celebrity status, while his energetic and powerful gestures captivate the audience's attention. The scene boasts a realistic approach with lifelike accuracy, showcasing the player's strong facial expressions and dynamic actions. Surrounding the player are cheering fans, waving colorful flags and banners, adding to the overall celebratory atmosphere. The artwork incorporates both graphic design and inspired illustrations, featuring a mix of light maroon and aquamarine colors. The flat background enhances the focus on the player, ensuring his moment of triumph is highlighted. The atmosphere is filled with pure joy and excitement, engulfing both the player and the spectators. --ar 16:9 --v 5.3
```
```text
/imagine prompt: A Brazilian football player, known for his exceptional skills, celebrates an extraordinary goal amidst a stadium filled with enthusiastic supporters. Dressed in a vibrant yellow jersey, the player raises his arms triumphantly in the air, his face radiant with happiness. The artist employs a combination of graphic design elements and inspired illustrations to bring the scene to life. With a realistic approach and lifelike accuracy, the artwork captures the player's strong facial expressions characterized by sheer joy and elation. As a backdrop, the stadium is depicted with flat backgrounds in light maroon and aquamarine hues, complemented by dark orange accents that emphasize the energy of the moment. The composition is dynamic and focuses on the player, showcasing his dynamic actions and energetic gestures. The overall mood is one of exuberance and celebration, captivating both football enthusiasts and admirers of graphic design. --ar 16:9 --v 5.3
```
```text
/imagine prompt: In a mesmerizing representation of a Brazilian football player celebrating an extraordinary goal, the artwork merges elements of graphic design and inspired illustrations. The player, adorned in a vivid yellow jersey, leaps into the air with his arms outstretched, basking in the adoration of the roaring crowd. The artist skillfully captures the player's facial expressions, granting lifelike accuracy through a realistic approach. The foreground showcases the player in the spotlight, while a flat background provides a serene yet vibrant setting in aquamarine and dark orange accents. The composition is full of dynamic elements, emphasizing the player's powerful and energetic gestures in capturing the essence of his accomplishment. The overall atmosphere exudes joy and triumph, encapsulating the thrill of the game and the celebration of a goal. --ar 16:9 --v 5.3
```
Главное здесь – исходная формула пользователя: `GTA style, ... flat backgrounds, strong facial expressions, dynamic actions` + **плоский однотонный фон** = узнаваемая раскладка загрузочного экрана.

**P058. Pixpretty: Classic Character Portraits (3)** – ChatGPT, Gemini, любой редактор · [Pixpretty / Tenorshare](https://pixpretty.tenorshare.ai/ai-insights/gta-style-ai-prompt.html)
```text
A gangster man with slicked-back hair and a black leather vest in a GTA 5 art style, with an urban alley background.
```
**P059.**
```text
Pale-skinned male biker with slicked-back blonde hair on a motorcycle in an arid desert, GTA V style.
```
**P060.**
```text
A Croatian woman in her 20s wearing professional attire, leaning on a security vehicle with cinematic GTA V lighting.
```

**P061. GTA Female Portrait (мотоцикл, закат)** – Midjourney · [The Prompt Index](https://www.thepromptindex.com/image-database.php?style=GTA) · картинка: `img/prompt-11-mj-motorbike-portrait.webp`
```text
a georgeous redhead young woman with blue eyes and full lips and fierce eyes with a motorbike and a sunset in los angeles in the style of a grand theft auto, loading screens ,GTA style artwork highly detailed, celshading, digital painting style, dramatic composition, 21st century comic book cover, studio lighting
```

**P062. Pixpretty: Detailed & Stylized (2)** – [Pixpretty](https://pixpretty.tenorshare.ai/ai-insights/gta-style-ai-prompt.html)
```text
Hyper-detailed character with tattoos and unique clothing, an expressive face, film-noir lighting, and GTA V realism.
```
**P063.**
```text
GTA 5-style illustration with cartoon vibes, bold lines, and exaggerated features.
```

**P064. Rugged Superstar Hero (текст в кадре)** – Nano Banana Pro (banana-pro) · [OOMOL Prompt Gallery](https://prompts.oomol.com/p/rugged-superstar-hero-illustration-884bb852)
```text
A digital illustration in the style of Grand Theft Auto loading screen art. A rugged, muscular Indian superstar sitting confidently in a wooden chair. He resembles a tough action hero with a thick beard, mustache, and wavy long hair, wearing aviator sunglasses. He is shirtless, revealing a toned torso with battle scars and scratches. His hands and wrists are wrapped in white boxing bandages. He is wearing white trousers. The background is a textured, grunge deep red. Behind his head, in large, bold, distressed yellow capital letters, is the text "INDIAN BIGGEST SUPERSTAR". The lighting is high-contrast with sharp shadows.
```
Структура «персонаж на однотонном грязно-красном фоне + крупная жёлтая надпись за головой» – прямо под обложку карусели.

---

## 2. Обложка-коллаж из панелей и загрузочный экран

Узнаваемая раскладка обложек серии с GTA III – сетка прямоугольных панелей с чёрными рамками, в каждой своя сцена. Для карусели это готовая обложка-первый слайд.

**P065. Nine-Panel Box-Art Collage** – ChatGPT · [Techpresso](https://academy.techpresso.co/prompts/chatgpt-prompts-gta)
```text
Transform [YOUR PHOTO] into a bold cel-shaded box-art collage in a gritty satirical street-game style. Keep my likeness recognizable. Build a 3x3 grid of illustrated comic panels framing different moments: my close-up portrait, a muscle car, a city skyline, a handgun silhouette, a helicopter, and palm trees, all in thick black outlines and flat saturated color. A wide horizontal title bar runs across the middle. Glossy game-cover composition, high contrast, 1:1 square.
```
Совет автора: вписать название города в полосу заголовка (`reads SUNSET CITY`). Для нас: пистолет заменить на ключ / магнитолу, полосу оставить пустой под русский текст.

**P066. Split-Panel Loading Screen** – ChatGPT · [Techpresso](https://academy.techpresso.co/prompts/chatgpt-prompts-gta)
```text
Reimagine [YOUR PHOTO] as a multi-panel loading-screen artwork in a saturated cel-shaded street-game style. Keep my likeness recognizable across the layout. Build a tall poster split into three vertical illustrated panels: a close-up of my determined face, a mid-shot of me leaning on a muscle car, and a wide shot of a gritty city block. Thick ink outlines, bold flat colors, dramatic shadows, satirical urban poster composition, 9:16 vertical.
```
Три панели «лицо мастера – мастер у машины – улица» = готовая история на один слайд.

**P067. Hero Cover Composition** – ChatGPT · [Techpresso](https://academy.techpresso.co/prompts/chatgpt-prompts-gta)
```text
Reimagine [YOUR PHOTO] as the central figure on a glossy game cover in a bold cel-shaded satirical style. Keep my face recognizable, posed front and center with arms crossed and confident attitude. Surround me with smaller illustrated vignettes of a sports car, a skyline at dusk, and a beach, all rendered in thick outlines and flat saturated color with hard shadows. A heavy game-logo banner sits at the top. Glossy retail-cover composition, 4:5 portrait.
```
Совет автора: `a bold price sticker in the corner` – наклейка с ценой, как на коробке. Для сервиса – наклейка «от 2 900 ₽» (текст ставить потом).

**P068. Strip-Collage Boulevard** – ChatGPT · [Techpresso](https://academy.techpresso.co/prompts/chatgpt-prompts-gta)
```text
Turn [YOUR PHOTO] into a horizontal strip-collage cover in a gritty cel-shaded open-world art style. Keep my likeness recognizable, placed at the left edge in a half-portrait. Stretch a continuous illustrated boulevard scene across the rest of the frame: palm trees, neon signs, a low-rider, and pedestrians, all in thick outlines and saturated flats with comic-grit shading. Cinematic widescreen poster composition, warm golden light, 16:9 landscape.
```

**P069. Diagonal-Slash Cover** – ChatGPT · [Techpresso](https://academy.techpresso.co/prompts/chatgpt-prompts-gta)
```text
Transform [YOUR PHOTO] into a dynamic cel-shaded game cover split by sharp diagonal slashes. Keep my likeness recognizable in the largest wedge with an intense expression. Fill the surrounding wedges with illustrated city fragments: a motorcycle, a skyscraper, a chain-link fence, all in thick black outlines and flat saturated color. Add bold halftone grit and a heavy stylized title across the bottom. Energetic satirical poster composition, high contrast, 4:5 portrait.
```

**P070. Special-Edition Embossed Cover** – ChatGPT · [Techpresso](https://academy.techpresso.co/prompts/chatgpt-prompts-gta)
```text
Reimagine [YOUR PHOTO] as a special-edition game-cover illustration in a bold cel-shaded satirical street style. Keep my face recognizable, rendered with thick outlines, flat saturated tones, and dramatic hard shadows over a dark moody backdrop with a faint city skyline. Add a faux embossed metallic title plate and a subtle gold border frame. Premium collector's-cover composition, glossy finish, high contrast, 4:5 portrait.
```
Подходит для «премиум-установки» (дорогая магнитола, звук).

**P071. Игровой постер-коллаж (Postium, промт 2)** – модель не указана (статья тестирует ChatGPT Images 2.0, Nano Banana 2, Qwen) · [Postium](https://postium.ru/promt-dlya-foto-v-stile-gta-6/)
```text
Convert this image into a 3:4 GTA VI-style game poster. Make the subject the central full-body playable character, standing confidently from an extreme low-angle view. Preserve facial likeness, pose, body proportions, recognizable clothing details and accessories, but restyle the outfit as a sharp GTA-style character costume with strong silhouette and clear poster readability. Use a bold cinematic collage composition: neon Miami-inspired coastal city, palm silhouettes, skyline, fast cars, street signs, nightlife lights and mission-like background vignettes where the same character appears in different action scenes. Build the background in layered graphic planes and keep the main character dominant. Style: official modern GTA VI promotional poster look — realistic but stylized face, clean jawline, angular features, crisp eyebrows, reduced skin microdetail, painterly digital illustration, sharp outlines, strong shadows, neon rim light, saturated colors. Color palette: warm magenta, teal-cyan, gold highlights and deep near-black shadows. Add glossy highlights, light bloom, subtle halftone grit, paper grain and controlled brush scuffs for authentic promo texture. Add one official-looking «Grand Theft Auto VI» title/logo area, placed once in the lower center or upper center, integrated into the poster. Avoid photorealistic live-action, anime, flat vector icons, retro film look, toy/chibi style.
```
Самое ценное – описание лица (`realistic but stylized face, clean jawline, angular features, crisp eyebrows, reduced skin microdetail`) и палитры (`warm magenta, teal-cyan, gold highlights and deep near-black shadows`). Строку про `«Grand Theft Auto VI» title/logo` – выкинуть.

**P072. «Vice City 2026» – сетка с панелями** – GPT Image 2 (хвост `--ar 2:3 --quality 2 --style raw` – от Midjourney, в GPT не работает) · [Carat, prompt 8511](https://carat.im/en/prompt-gallery/p/8511) **(анти-пример по правам, ценный по структуре)**
```text
Create a stylized AAA video game key art poster.
CONCEPT:
“Vice City 2026” reimagined — modern evolution of the iconic GTA Vice City cover art. Preserve the comic-panel collage identity, but upgrade with futuristic Miami, tech culture, and modern crime lifestyle.
STYLE:
AAA game key art, Unreal Engine 5 inspired rendering + illustrated comic-panel hybrid
Bold black grid layout, sharp vector framing, stylized GTA-like characters (NOT real humans)
High-saturation neon palette (magenta, cyan, electric blue, sunset orange)
FORMAT:
Classic GTA cover grid composition (multi-panel collage with thick black dividers)
Centered stacked title typography
────────────────────────────
🧩 PANEL COMPOSITION (MODERNIZED ICONIC GRID):
Top-left:
Police helicopter redesigned as a sleek surveillance drone chopper with neon accents, flying over futuristic Miami skyline
Top-center:
Stylized male character (Tommy-inspired 2026 version) holding a smartphone instead of cash — crypto trading UI glow on screen
Top-right:
High-performance futuristic superbike (Tron-inspired neon trims), aggressive angle
Mid-left:
Stylized female NPC in modern beachwear (tasteful, confident), holding phone taking selfie with neon skyline behind
Center:
Large bold stacked title:
“grand theft auto” (classic block typography)
“vice city” in neon script
Add “2026” subtle tag integrated into script glow
Mid-right:
Luxury hypercar (Infernus-inspired redesign), sharp LED strips, aggressive stance
Bottom-left:
New protagonist portrait (Tommy-inspired, older, dominant expression, modern outfit)
Bottom-center:
High-speed car chase panel — car flipping mid-air with sparks, police drones + neon VCPD vehicles chasing
Bottom-right:
Stylized character (Lance-inspired 2026), holding futuristic weapon, confident stance
Additional small panels (optional fill-ins):
- Jet ski cutting through neon ocean water
- AI billboard with crypto ads
- Nightclub silhouette scene with dancers
- Beach lifeguard tower glowing neon
────────────────────────────
🎨 ART DIRECTION:
Color:
- Strong contrast neon palette
- Pink/cyan split lighting across panels
- Warm sunset gradients for beach panels
Lighting:
- Hard comic-style highlights + UE5 glow effects
- Neon reflections and rim lighting
Texture:
- Slight grain + halftone comic texture overlay
- Clean vector edges with subtle 3D depth
────────────────────────────
🔤 TYPOGRAPHY:
“grand theft auto” — bold white stacked block font (iconic style)
“vice city” — neon script, glowing pink with cyan edge
“2026” — small futuristic numeric tag integrated subtly
────────────────────────────
🎥 CAMERA / FRAMING:
Each panel:
- Dynamic angles (low-angle cars, close-up portraits, action tilt shots)
- Cinematic composition inside each frame
────────────────────────────
✨ PLAYFUL DETAILS:
- Crypto/AI billboards instead of retro ads
- Police drones instead of only cars
- Smartphone glow replacing old-school pager/cash vibe
- Neon reflections exaggerated for game aesthetic
- Subtle HUD/UI hints embedded in panels
────────────────────────────
RENDER DETAILS:
Ultra-detailed stylized assets, crisp outlines, vibrant lighting, clean separation between panels
NEGATIVE:
real humans, photoreal poster, movie poster style, flat illustration only
OUTPUT:
--ar 2:3 --quality 2 --style raw
```
Брать: блочную раскладку «позиция панели → что в ней», раздел ART DIRECTION, `thick black dividers`, `clean separation between panels`. Не брать: название игры, персонажей (Томми, Лэнс), Infernus.

**P073. Коллаж-обложка Vice City (рус.)** – любой сервис с фото · [Directline](https://www.directline.pro/connect/p/prompt-dlya-foto-v-stile-gta/)
```text
Создай картинку в формате коллажной обложки в стиле ГТА Vice City. В центре — крупный погрудный портрет человека с загруженного фото, лицо узнаваемое, выражение уверенное. Если мужчина — голубая гавайская рубашка, зачесанные назад волосы; если женщина — белый топ, крупные серьги, волосы в стиле 80-х. Вокруг портрета — мозаика из прямоугольных панелей: девушка в бикини на фоне пальм, погоня на спорткаре, неоновая вывеска, вертолет над городом, закат. Палитра: розовый, фиолетовый, бирюзовый. Стиль: рисованная иллюстрация Rockstar, контуры, cel-shading. Не генерируй: 3D-рендер, фотореализм, темные тона, размытие, деформацию черт лица, лишние пальцы.
```

**P074. Коллаж-обложка GTA V (рус.)** – любой сервис с фото · [Directline](https://www.directline.pro/connect/p/prompt-dlya-foto-v-stile-gta/)
```text
Создай изображение в формате коллажной обложки GTA V. В центре — крупный погрудный портрет человека с загруженного фото, лицо узнаваемое. Если мужчина — темные очки-авиаторы, расстегнутая рубашка; если женщина — солнцезащитные очки, легкий топ. Вокруг портрета — прямоугольные панели с типичными сценами GTA V: девушка в бикини с телефоном, полицейская погоня, вертолет, яхта, ограбление в масках, Вайнвуд-Хиллз. Палитра: голубой, белый, зеленый, оранжевый. Стиль: фирменная иллюстрация Rockstar, рисованные контуры, высокий контраст. Логотип «V» в верхней части. Не генерируй: пиксельную графику, темную палитру, фотореализм, размытие, деформацию лица, лишние пальцы.
```
`Логотип «V»` – убрать.

**P075. GTA San Andreas Indonesian Style (JSON)** – GPT Image 2 · [YouMind](https://youmind.com/prompts/gta-san-andreas-indonesian-poster-26846)
```text
{"style": "Highly detailed GTA San Andreas-inspired cinematic poster illustration with modern urban editorial aesthetics, bold comic-book shading, dramatic lighting, rich contrast, vivid color grading, layered textures, graffiti details, sticker graphics, distressed poster textures, premium typography, and dynamic street-style composition. Ultra-detailed 8K render quality.", "subject": {"description": "Young charismatic man with curly hair, beard, and glasses, portrayed as the central focal point in a modern GTA San Andreas loading-screen inspired artwork.", "pose": "Relaxed yet confident seated pose with expressive natural body language, slightly leaning forward with one hand near the chin, giving a stylish international fashion-model vibe.", "expression": "Confident, charismatic, friendly smile with strong personality and modern urban attitude.", "outfit": {"style": "Modern premium streetwear fashion", "details": ["Layered varsity jacket", "Oversized hoodie", "Graphic typography elements", "Streetwear patches", "Luxury casual accessories", "Chain necklace", "Modern watch"], "colors": ["dark green", "cream white", "black", "gold accents"], "materials": ["wool", "cotton", "leather textures"]}}, "background": {"theme": "Dynamic Indonesian urban atmosphere mixed with GTA San Andreas cinematic environment", "landmarks": [{"name": "Monas", "city": "Jakarta"}, {"name": "Gedung Sate", "city": "Bandung"}, {"name": "Borobudur Temple", "city": "Yogyakarta"}, {"name": "Suramadu Bridge", "city": "Surabaya"}, {"name": "Pura Ulun Danu", "city": "Bali"}], "elements": ["sunset cinematic sky", "urban skyline", "palm trees", "classic lowrider car", "graffiti walls", "street poster textures", "editorial collage overlays", "sticker graphics", "paint splashes", "grunge textures", "comic ink outlines"]}, "typography": {"main_title": "Kings Landing", "subtitle": "Indonesia Is My Playground", "style": "Bold premium urban typography inspired by GTA San Andreas promotional artwork", "details": ["layered title composition", "distressed fonts", "street-style lettering", "graffiti-inspired accents", "sticker typography", "dynamic hierarchy", "modern editorial placement"]}, "lighting": {"style": "Cinematic dramatic sunset lighting", "details": ["high contrast shadows", "warm orange glow", "deep blacks", "golden highlights", "soft atmospheric haze"]}, "composition": {"layout": "Highly engaging non-generic poster layout with layered depth and asymmetrical balance", "camera_angle": "Medium close-up with cinematic perspective", "render_quality": "Ultra detailed 8K", "mood": ["vibrant", "cinematic", "stylish", "premium", "urban", "modern", "energetic"]}, "art_direction": {"inspirations": ["GTA San Andreas loading screens", "modern streetwear campaigns", "urban editorial posters", "comic-book illustration", "luxury urban branding"], "avoid": ["flat composition", "stiff pose", "minimal details", "generic typography", "plain clothing", "empty background"]}}
```
**Прямая заготовка под «Новосибирск – моя игровая площадка»**: в `landmarks` – Оперный театр, Коммунальный мост, Академгородок; заголовок – свой, без названия игры.

**P076. GTA V Style Crossover Cover Art (JSON)** – GPT Image 2 · [YouMind](https://youmind.com/prompts/gta-v-style-crossover-cover-art-13555) **(анти-пример: чужой персонаж и логотипы)**
```text
{
 "type": "video game cover art collage",
 "style": "GTA V cover art style, cel-shaded illustration, thick black panel borders",
 "centerpiece": {
 "character": "Thomas Shelby from Peaky Blinders, wearing dark suit, white shirt, smoking cigarette, undercut hairstyle",
 "logo": "grand theft auto V logo with green V and FIVE banner",
 "subtitle": "THOMAS SHELBY BIRMINGHAM. 1919."
 },
 "layout": {
 "panel_count": 8,
 "panels": [
 {
 "position": "top-left",
 "description": "Hillside with VINEWOOD sign, radio tower, palm trees"
 },
 {
 "position": "upper-left",
 "description": "Street sign reading SMALL HEATH BIRMINGHAM S 41, terraced houses"
 },
 {
 "position": "mid-left",
 "description": "Handgun, 3 bullets, map with text 'BY ORDER OF THE PEAKY BLINDERS'"
 },
 {
 "position": "bottom-left",
 "description": "Vintage 1920s black car, glowing headlights, 'GTA V' license plate"
 },
 {
 "position": "top-right",
 "description": "City skyline silhouette, helicopter"
 },
 {
 "position": "mid-right",
 "description": "3 men in flat caps and suits walking in smoky industrial setting"
 },
 {
 "position": "bottom-right-upper",
 "description": "Large country mansion, black horse on lawn"
 },
 {
 "position": "bottom-right-lower",
 "description": "Man in flat cap looking at industrial skyline, yellow Rockstar Games logo"
 }
 ]
 }
}
```
Структура JSON «панель → позиция → описание» – удобна; содержание – чужие персонажи и знаки.

**P077. GTA Stylizer (системный промт GPT из магазина GPTs)** – ChatGPT / DALL-E 3 · [GitHub, LouisShark/chatgpt_system_prompt](https://github.com/LouisShark/chatgpt_system_prompt/blob/main/prompts/gpts/ostR6TTNg_GTA_Stylizer.md)
```text
You are GTA Style GPT. The style depicted in the art  you create is reminiscent of the distinctive art used in the marketing and presentation of the Grand Theft Auto (GTA) video game series. Here's a detailed breakdown of this style:

1. **Digital Illustration with Bold Line Work**: The images showcase crisp and bold line work, which defines the outlines of characters, objects, and scenery. The lines are confident and vary in thickness, giving a sense of depth and form.

2. **Vibrant, Saturated Colors**: The color palette is vibrant and highly saturated, with a rich contrast between colors. This results in a dynamic and energetic visual that stands out, with almost a neon-like quality to some elements.

3. **Stylized Realism**: The overall aesthetic leans towards stylized realism. While proportions and scenarios are based on real-world references, there is a certain exaggeration in features and expressions to enhance the visual impact.

4. **Dramatic Lighting and Shadows**: There is a stark use of lighting and shadows, with high contrast that creates a dramatic mood. The shadows are often used to accentuate the three-dimensionality of the subjects.

5. **Pop Culture Infusion**: The art style heavily borrows from pop culture elements, with a clear nod to contemporary and retro aesthetics, reminiscent of comic book art or 80s-90s action movie posters.

6. **Detailed Textures and Patterns**: Surfaces and materials are rendered with considerable attention to texture. Fabric patterns, reflections on metal or glass, and environmental details like snow or explosions are rendered with high fidelity.

7. **Dynamic Composition**: Each scene is composed to convey action and narrative, often with dynamic poses, interesting angles, and elements that guide the viewer’s eye throughout the image.

8. **Caricature and Satire**: Characters and scenarios often include elements of caricature, with exaggerated features or situations that play on stereotypes or satirical takes on societal themes.

9. **Cinematic Influence**: The scenes are set up in a cinematic style, with the positioning of characters and the environment resembling a movie scene or a storyboard panel.

10. **Narrative Element**: Each piece tells a story or hints at a larger narrative, inviting the viewer to infer the backstory or the events that are unfolding.

This style is distinctly modern and has a mass appeal due to its connection with the iconic video game series. 

You are to generate wide format, HD images from the user's description in this style. 
```
Дана середина системного промта (без «мотивационного» вступления). Готовый словарь из 10 признаков стиля – можно вставить в «Проект» ChatGPT как постоянную инструкцию.

---

## 3. Машина, тюнинг, гараж, мастер

**P078. Street Racer** – ChatGPT · [Techpresso](https://academy.techpresso.co/prompts/chatgpt-prompts-gta)
```text
Transform [YOUR PHOTO] into a street-racer character in a gritty cel-shaded open-world art style. Keep my likeness recognizable, dressed in a fitted racing jacket and fingerless gloves, leaning casually against a tuned import car with neon underglow. Thick black outlines, flat saturated color, hard shadows, and a hazy nighttime garage strip behind me. Confident smirk, satirical urban poster cropping, high contrast, 4:5 portrait.
```
Совет автора: назвать машину конкретно (`matte-black muscle car`, `orange drift coupe`).

**P079. Main Character at Sunset (человек у спорткара)** – image-to-image (ChatGPT, Gemini, Media.io) · [Media.io](https://www.media.io/ai/explore/zone/gta-6-loading-screen-ai-generator)
```text
Image Prompt: Main Character at Sunset. Use the uploaded photo as the identity and clothing reference for a GTA 6-inspired character poster. Preserve the person’s recognizable face, hairstyle, skin tone, build and outfit. Show one person from the knees up in a relaxed, confident three-quarter pose beside a parked sports car. Place the car slightly behind them without covering their face or hands. Set the scene on a Miami-inspired coastal boulevard with palm trees, pastel art-deco buildings and a vivid pink-orange sunset. Render everything as a cohesive digital illustration with bold black contours, semi-realistic facial details, cel-shaded colors and hard-edged shadows. Use coral, magenta and turquoise accents. Vertical 9:16 composition, with the person as the focal point. No text, logos, watermark, game HUD or additional people.
```
**Лучший образец «человек + машина»**: чётко разведены лицо, машина, фон, техника, палитра, формат, запреты. Шаблон Ш1 ниже сделан из него.

**P080. Тюнинг-культура, LS Car Meet (рус.)** – любой сервис с фото · [Directline](https://www.directline.pro/connect/p/prompt-dlya-foto-v-stile-gta/)
```text
Воспроизведи внешность человека с загруженного фото. Стилизуй под арт GTA Online, тематика — LS Car Meet. Подземная парковка, залитая цветным неоновым светом. Человек стоит, опираясь на капот тюнингованного спорткара. Если мужчина — гоночная куртка, перчатки, кепка козырьком назад; если женщина — укороченная мотокуртка, высокие ботинки, спортивные очки на голове. Вокруг — другие тюнингованные машины, дым от покрышек, неоновая подсветка. Палитра: неоново-синий, красный, черный, хромовые блики. Стиль: рисованная иллюстрация Rockstar, жесткие контуры, высокий контраст. Не генерируй: дневной пейзаж, сельскую местность, ретроавтомобили, пиксельную графику, деформацию лица, лишние пальцы.
```
Ближе всего к нашему боксу: закрытое помещение, неон, машина, человек у капота – не нужны ни пальмы, ни лето.

**P081. Ночной Лос-Сантос (GTA Online, рус.)** – любой сервис с фото · [Directline](https://www.directline.pro/connect/p/prompt-dlya-foto-v-stile-gta/)
```text
Воспроизведи внешность человека с загруженного фото. Стилизуй под промоарт GTA Online. Ночной Лос-Сантос: неоновые огни, небоскребы, суперкар с подсветкой днища. Рисованный стиль Rockstar с яркими насыщенными цветами и жесткими контурами. Если мужчина — костюм с экстравагантным рисунком, светящиеся кроссовки, маска на лбу; если женщина — блестящий комбинезон, неоновые аксессуары, яркий макияж. Вокруг — хаос: взрывы на заднем плане, летящий мотоцикл Oppressor в небе, деньги в воздухе. Палитра: неоново-зеленый, ярко-розовый, фиолетовый, черный. Не генерируй: реалистичную фотографию, спокойную атмосферу, приглушенные цвета, деформацию лица, лишние конечности, размытие.
```

**P082. Мастер с ключом на плоском фоне (эталон для сервиса)** – GTA Style LoRA, триггер `gt9style`, вес 0.6 (база в карточке – MOSS Image) · [Civitai, модель 66719](https://civitai.com/models/66719) · картинка: `img/prompt-05-civitai-mechanic.webp`
```text
This digital illustration depicts a rugged young man wearing a sleeveless work shirt, mechanic gloves, and faded jeans, holding a wrench over his shoulder. He has short messy hair and a slightly mischievous expression. The background is a solid mustard yellow color with silhouettes of garages, car engines, and industrial tools.
```
Параметры с картинки: 8 шагов, CFG 1, Euler, 1024×1536. **Главная находка**: формула «персонаж + сплошной цветной фон + силуэты по теме» и есть раскладка загрузочного экрана. Работает и без LoRA, если дописать технику (контур, cel-shading).

**P083. Парень в белой футболке (та же серия)** – та же LoRA · [Civitai 66719](https://civitai.com/models/66719)
```text
This digital illustration depicts a young man wearing a white oversized T-shirt, gold chain, dark jeans, and sneakers, standing confidently with one hand in his pocket. He has a serious expression and wears stylish sunglasses. The background is a solid warm orange color with silhouettes of palm trees, city buildings, and street lamps.
```

**P084. Чёрный суперкар крупно** – Flux.1 Dev + LoRA `aidmaGTA6` · [Civitai, модель 688840](https://civitai.com/models/688840) · картинка: `img/prompt-06-civitai-supercar.webp`
```text
A dramatic close-up of a sleek black supercar under low light, with sharp reflections, glowing LED headlights, matte and glossy textures, aggressive front design, carbon fiber details, cinematic shadows, and a dark moody background — ultra-realistic, high contrast, mysterious atmosphere. aidmaGTA6
```
30 шагов, CFG 3.5. Результат – фото, не рисунок: `ultra-realistic` перебил LoRA.

**P085. Две машины на мокрой ночной улице** – Flux.1 Dev + `aidmaGTA6` · [Civitai 688840](https://civitai.com/models/688840) · картинка: `img/prompt-07-civitai-wet-road.webp`
```text
a high-resolution, cinematic-style photograph depicting a nighttime urban street scene. The layout is vertical, focusing on two sleek sports cars driving down a wet, reflective road. The foreground features a white sports car with distinctive round red taillights and a glossy finish, emitting exhaust vapor. In the background, another similar car is visible, slightly blurred, enhancing the sense of motion. The street is lined with tall buildings adorned with bright neon signs in various colors, including blue and white, adding a vibrant, futuristic atmosphere. Streetlights cast a cool, bluish glow, reflecting off the wet pavement. A few pedestrians are visible on the sidewalk, but their features are not discernible. The overall mood is dynamic and modern, capturing the essence of a bustling city nightlife.
 aidmaGTA6
```
Слово `photograph` в начале = фото на выходе. Урок.

**P086. Классический маслкар маслом** – Flux.1 Dev + `aidmaGTA6` · [Civitai 688840](https://civitai.com/models/688840)
```text
A nostalgically crafted relic of the past, a meticulously restored deep silver pearlescent classic 60's muscle car cruises through the dusk streets with an intimidating elegance. The vintage vehicle gleams with a lustrous sheen, showcasing its aerodynamic lines and sharp accents as it cruises along the asphalt. This evocative scene is captured in a vividly detailed oil painting, where every brushstroke highlights the car's classic styling and pristine condition. Impeccably rendered, this image transports viewers to a bygone era of automotive luxury and style. aidmaGTA6
```

**P087. Кабриолет на обрыве** – Flux.1 Dev + `aidmagta6` · [Civitai 688840](https://civitai.com/models/688840)
```text
aidmagta6,    luxury convertible parked on a coastal cliff: at sunset, a woman in a flowing red scarf stands beside the car, wind teasing the fabric around her waist, one hand on the door, the other brushing her lips
```
35 шагов, CFG 3.5, Euler, 720×1280. Триггер в начале.

**P088. Угнанная машина и погоня** – Flux.1 Dev + `aidmaGTA5` + `aidmaHyperrealism` · [Civitai 688840](https://civitai.com/models/688840) **(тема не для сервиса)**
```text
A chaotic street scene with pedestrians scattering as a stolen car speeds by, pursued by law enforcement, tires screeching and engines roaring.
,aidmaHyperrealism, aidmaGTA5
```

**P089. Машина на ночной улице (drawing gta style)** – SDXL-эпоха, LoRA `drawing gta style v2` вес 0.8 · [Civitai, модель 558832](https://civitai.com/models/558832) · картинка: `img/prompt-16-civitai-car-night.webp`
```text
UHD, 4k, ultra detailed, cinematic, a photograph of  <lora:drawing gta style v2:0.8>
realistic art style a car driving down a city street at night, perfect image, sharp image, detailed image, vivid color style, bright tone, high color constrat, high saturation, high quality image style, 80's style, 90's style, cinematic art style, grand theft auto art style, outdoors, sky, no humans, night, ground vehicle, building, scenery, motor vehicle, city, car, road, cityscape, lamppost, street, city lights, crosswalk, window, night sky, light, vehicle focus, lights, tree, dark, reflection, skyscraper, epic, beautiful lighting, inpsiring
```
Негатив: `ugly, deformed, noisy, blurry, low contrast, realistic`. 25 шагов, CFG 1, Euler. Опять `a photograph of` + `realistic art style` → фото.

**P090. Машина среди взрывов** – Z-Image Turbo + LoRA `GTA style zib v1` вес 1 · [Civitai 558832](https://civitai.com/models/558832)
```text
cinematic film still of  <lora:GTA style zib v1:1>
Digital drawing art style a car is driving down a street with a lot of fire explosions, perfect image, sharp image, detailed image, vivid color style, bright tone, high color, high saturation, high quality image style, 80's style, 90's style, cinematic art style, grand theft auto art style, outdoors, tree, no humans, fire, ground vehicle, building, motor vehicle, smoke, city, palm tree, car, explosion, vehicle focus, debris, destruction, truck, sky, cloud, motion blur, road, dust, sports car, scenery, lamppost, glowing
, shallow depth of field, vignette, highly detailed, high budget, bokeh, cinemascope, moody, epic, gorgeous, film grain, grainy
```
Негатив в разделе 7. 10 шагов, CFG 1, 1920×1080.

**P091. Человек у синей машины на пляже (SDXL, три LoRA)** – SDXL + `GTAVstyleDoguXL:0.95`, `GTA VI Style:0.9`, `ClassicMuscleCar1-XL:0.55` · [Civitai, модель 119307](https://civitai.com/models/119307)
```text
(masterpiece), (best quality), A handsome young muscular Indian man with perfect face and perfectly chiseled body wearing pink gown standing in front of a blue car near sea beach <lora:GTAVstyleDoguXL:0.95> <lora:GTA VI Style:0.9> GTA screenshot, unreal engine 5,  gta gameplay in miami <lora:COMFYUI_mimic_landscape_-_XL_SDXL v2.0:0.55> <lora:ClassicMuscleCar1-XL:0.55> ClassicMuscleCar <lora:1980's style:0.55> 1980's style, masterful composition, dynamic volumetric lighting, realistic  ray_tracing, reflection, hyperrealistic, shallow depth of field, f/2.4, bokeh,
```
Пример смешивания LoRA с весами 0.55–0.95; длинный негатив – в разделе 7. 30 шагов, CFG 3.5, DPM++ 2M SDE.

**P092. G Wagon на пирсе** – DALL-E · [The Prompt Index](https://www.thepromptindex.com/image-database.php?style=GTA) · картинка: `img/prompt-09-dalle-gwagon.webp`
```text
Mercedes G wagon in the style of GTA 5 loading screen art, parked up at the pier. ferris wheel in background.
```

**P093. Audi Q7** – DALL-E · [The Prompt Index](https://www.thepromptindex.com/image-database.php?style=GTA)
```text
Audi Q7 SUV in the style of GTA 5 loading screen art, crusing through the streets of los santos at night.
```

**P094. Volvo XC90** – DALL-E · [The Prompt Index](https://www.thepromptindex.com/image-database.php?style=GTA)
```text
Volvo XC90 SUV in the style of GTA 5 loading screen art, crusing through vinewood hills.
```

**P095. Ford Ranger** – DALL-E · [The Prompt Index](https://www.thepromptindex.com/image-database.php?style=GTA) · картинка: `img/prompt-10-dalle-ford-ranger.webp`
```text
Ford Ranger Truck in the style of GTA 5 loading screen art, on the dusty dirt roads of mount chilliad.
```

**P096. Camaro** – DALL-E · [The Prompt Index](https://www.thepromptindex.com/image-database.php?style=GTA)
```text
Chevrolet Camaro, races through the vibrant streets of downtown Los Santos. This image prompt combines the dynamic art style of GTA with the timeless design and power of the Camaro, creating a captivating visual experience.
```

**P097. Morris Minor** – DALL-E · [The Prompt Index](https://www.thepromptindex.com/image-database.php?style=GTA)
```text
front angle morris minor in the style of GTA 5 loading screen art, driving through los santos at night.
```

**P098. Citroen Saxo** – DALL-E · [The Prompt Index](https://www.thepromptindex.com/image-database.php?style=GTA)
```text
Citroen Saxo 2001 model, in the style of GTA 5 loading screen art
```

**P099. Nissan Skyline ночью** – DALL-E · [The Prompt Index](https://www.thepromptindex.com/image-database.php?style=GTA)
```text
front angle nissan skyline in the style of GTA 5 loading screen art, driving through los santos at night.
```

**P100. Nissan Skyline сбоку** – DALL-E · [The Prompt Index](https://www.thepromptindex.com/image-database.php?style=GTA)
```text
side angle nissan skyline in the style of GTA 5 loading screen art, driving through los santos.
```

**P101. Porsche на горном серпантине** – DALL-E · [The Prompt Index](https://www.thepromptindex.com/image-database.php?style=GTA)
```text
Rear Angle Porsche 911 in the style of GTA 5 loading screen art, driving through Mountainous Curved Roads of mount chilliad adds an element of thrill and adventure.
```

**P102. GTA style Porsche (с опечаткой автора)** – DALL-E · [The Prompt Index](https://www.thepromptindex.com/image-database.php?style=GTA)
```text
Porsche 911 in the style of GRA 5 loading screen art
```
Формула DALL-E-серии: `[марка модель] + [ракурс: front / side / rear angle] + in the style of GTA 5 loading screen art + [где едет]`. Самая простая заготовка под «машину клиента» – см. шаблон Ш2.

**P103. Convertible Cruise** – ChatGPT · [Techpresso](https://academy.techpresso.co/prompts/chatgpt-prompts-gta)
```text
Reimagine [YOUR PHOTO] cruising in an open-top convertible in a bold cel-shaded street-game style. Keep my face recognizable behind the wheel, one arm resting on the door, sunglasses on. Thick outlines, flat saturated color, palm trees blurring past, and a vivid sunset boulevard with neon signs and other cars. Motion smears for speed, satirical urban poster composition, warm light, 16:9 landscape.
```

**P104. Gas-Station Standoff** – ChatGPT · [Techpresso](https://academy.techpresso.co/prompts/chatgpt-prompts-gta)
```text
Turn [YOUR PHOTO] into a gritty cel-shaded gas-station scene in a satirical open-world art style. Keep my likeness recognizable, leaning against a vintage fuel pump under a buzzing fluorescent canopy at dusk. Thick black outlines, flat saturated tones, harsh artificial light pooling on the asphalt, and a lonely desert-edge highway with a dim sky behind. Cinematic noir-ish poster cropping, comic grit, high contrast, 4:5 portrait.
```
Заправка под люминесцентным навесом – готовая «зимняя ночная» сцена, если пустыню заменить на снег.

**P105. Convertible Couple Cruise** – ChatGPT · [Techpresso](https://academy.techpresso.co/prompts/chatgpt-prompts-gta)
```text
Transform [YOUR PHOTO WITH TWO PEOPLE] into a cel-shaded couple cruising in a convertible in a saturated satirical street style. Keep both faces recognizable, one driving and one riding with an arm raised, sunglasses on. Thick black outlines, flat vivid color, palm trees blurring past, motion smears, and a glowing sunset boulevard. Warm cinematic poster composition, high contrast, 16:9 landscape.
```

**P106. GTA VI Motorcycle Character Poster (свой текст в кадре)** – GPT Image 2 · [YouMind](https://youmind.com/prompts/gta-vi-character-poster-28022)
```text
Using the provided reference image, transform the person on the motorcycle into a Grand Theft Auto VI / Vice City inspired illustrated poster. Preserve the rider’s recognizable identity, pose, sunglasses, white jacket with the large “P” patch, jeans, shoes, and the motorcycle as the main subject, but stylize everything as polished game key art with bold outlines, glossy highlights, saturated neon colors, and dramatic cel-shaded rendering.
Change the setting from the forest roadside to a tropical coastal city at sunset: add a wide boulevard, palm trees, pastel art-deco buildings, ocean water, a distant skyline, and a warm pink-orange-to-blue gradient sky with soft clouds. Make the motorcycle look slightly more heroic and pristine with reflective chrome and teal/pink neon rim lighting. Use a low-angle poster composition with the rider and bike large in the foreground, facing slightly right.
Add exactly 2 visible text/logo elements: 1) large block title text in the bottom-left reading LEONIDA STATE; 2) a small semi-transparent badge/logo in the top-right reading FICTIONAL LIFESTYLE STUDIO. Keep the overall mood cinematic, tropical, stylish, and like official open-world crime game promotional artwork. No photorealism, no extra people, no clutter.
```
Приём «ровно 2 текстовых элемента, вот какие и где» – правильный способ управлять текстом в GPT Image. Под нас: `reading NOVOSIBIRSK` + свой бейдж сервиса.

**P107–P110. Pixpretty: машины (4)** – ChatGPT, Gemini, любой редактор · [Pixpretty](https://pixpretty.tenorshare.ai/ai-insights/gta-style-ai-prompt.html)
```text
Sports car speeding on a freeway at sunset with motion blur, GTA V-style artwork.
```
```text
An action hero standing beside a getaway car with dramatic shadows, bold lines, and vibrant colors, GTA-style.
```
```text
Custom lowrider on a sunny Los Santos street, GTA San Andreas style, colorful and vibrant.
```
```text
A rugged off-road vehicle splashing through mud in Blaine County, in a gritty and realistic GTA V style.
```

**P111–P112. Midjourney: гараж и перекраска** – Midjourney · [Magica, 23 Midjourney Prompts for Grand Theft Auto](https://magica.com/blog/midjourney-prompts-for-grand-theft-auto)
```text
A stolen car being dismantled in a chop shop, parts scattered, mechanics at work.
```
```text
A classic muscle car, stolen and repainted, given a new identity, vintage charm.
```
В этих промтах нет ни одного слова о стиле – только сюжет. Модель выдаст обычную картинку, «GTA» не получится. Показательный пример слабого промта. Ещё 21 сцена из той же статьи – про угон и погони, для сервиса не берём (в счёт не включены).

---

## 4. Город, закат, неон, пальмы

**P113. Rooftop Skyline Overlook** – ChatGPT · [Techpresso](https://academy.techpresso.co/prompts/chatgpt-prompts-gta)
```text
Transform [YOUR PHOTO] into a cel-shaded city-scene illustration in a gritty satirical street-game style. Keep my likeness recognizable, standing on a rooftop ledge overlooking a sprawling sun-hazed metropolis at golden hour. Thick black outlines, flat saturated color, hard long shadows, and a skyline of skyscrapers, billboards, and palm-lined avenues below. Wide cinematic establishing-shot composition, warm light, high contrast, 16:9 landscape.
```

**P114. Neon Alley After Dark** – ChatGPT · [Techpresso](https://academy.techpresso.co/prompts/chatgpt-prompts-gta)
```text
Transform [YOUR PHOTO] into a nighttime back-alley city scene in a saturated cel-shaded satirical style. Keep my face recognizable, lit by neon signs and a flickering streetlight casting hard colored shadows. Thick ink outlines, flat vivid color, rain-slicked pavement reflecting pink and cyan glow, dumpsters and fire escapes framing the alley. Cinematic gritty poster composition, atmospheric haze, high contrast, 4:5 portrait.
```

**P115. Diner Booth Hangout** – ChatGPT · [Techpresso](https://academy.techpresso.co/prompts/chatgpt-prompts-gta)
```text
Reimagine [YOUR PHOTO] sitting in a retro diner booth in a bold cel-shaded street-game style. Keep my likeness recognizable, leaning back with a coffee cup, neon diner sign glowing through the window behind me. Thick outlines, flat saturated color, warm interior light against a cool night outside, chrome and checkerboard details. Satirical urban poster composition, comic grit texture, high contrast, 4:5 portrait.
```
`warm interior light against a cool night outside` – формула нашей «клиентской зоны зимой».

**P116. Retro Miami GTA-Style Character Poster** – GPT Image 2 · [YouMind](https://youmind.com/prompts/retro-miami-character-poster-24174) · картинка: `img/prompt-14-youmind-retro-miami.webp`
```text
Create a full-body illustrated poster of a confident 1980s Miami crime-drama protagonist in a GTA V-inspired American retro promotional art style. The character is a stylish adult man with dark slicked-back wavy hair, standing in a relaxed power pose, facing slightly left while looking forward; keep his face area intentionally obscured by a soft rectangular blur as if anonymized. He wears a cream-white suit with broad shoulders and sharp black ink outlines, a vivid coral-red open-collar dress shirt, a dark belt, cream trousers, and white shoes. His left hand is down by his side and his right hand holds a lit brown cigar with curling smoke. Set him on a neon tropical boulevard at sunset in 1980s Miami, with exactly 8 visible palm trees: 2 large framing palms at the top left and top right, 2 tall skinny palms on the right side, 1 tall palm on the far left, and 3 smaller background palms along the street. Include a colorful low-rise art deco building on the lower right with orange, teal, and magenta accents, a bright pink-orange road or sidewalk in the foreground, and a turquoise-to-yellow sky with diagonal sunlit streaks. Use bold comic-book linework, saturated teal, cyan, magenta, orange, and yellow colors, dramatic cel shading, high contrast, glossy poster finish, dynamic perspective from slightly below, vertical composition, no text, no logo, no watermark.
```
Промт просил размыть лицо – модель нарисовала лицо, похожее на известного актёра. Вывод: «узнаваемый типаж 80-х» тянет за собой чужое лицо; лучше давать фото своего мастера.

**P117. Retro Miami Sunset Poster** – ChatGPT · [Media.io](https://www.media.io/image-effects/chatgpt-gta-style-poster-prompts.html)
```text
Create a retro GTA VI Miami sunset poster featuring pastel orange skies and glowing neon reflections across wet surfaces. Include palm silhouettes, vintage sports car, cinematic grain texture, tropical atmosphere, and 1980s synthwave energy throughout the composition. Deliver bold game-poster composition with hyper detailed promotional artwork aesthetic that evokes classic Rockstar nostalgia.
```

**P118. Downtown night (с параметрами MJ)** – Midjourney v5.2 · [The Prompt Index](https://www.thepromptindex.com/image-database.php?style=GTA)
```text
cairo city from the street, Miami mode, GTA San Andreas Mod, at night, neon purple lights, 4k --s 750 --v 5.2
```
Единственный найденный MJ-промт с `--s` (stylize 750 = сильная стилизация).

**P119. Город на закате** – Flux.1 Dev + `aidmaGTA6` + `aidmaHyperrealism` · [Civitai 688840](https://civitai.com/models/688840)
```text
A sprawling cityscape at sunset, with towering skyscrapers casting long shadows, and the sky painted in hues of orange and pink.
,aidmaHyperrealism, aidmaGTA6
```

**P120. Мокрая ночная улица, фигура у переулка** – Flux.1 Dev + `aidmaGTA5` + `aidmanijiv6` · [Civitai 688840](https://civitai.com/models/688840)
```text
gritty urban landscape at night, with neon lights reflecting off wet streets, and a lone figure walking towards a dimly lit alley, their shadow stretching long behind them.
,aidmaGTA5, aidmanijiv6
```

**P121. У ночного клуба, чернильный стиль** – Flux.1 Dev fp8 + `aidmaGTA5Style:1` + `aidmaInkStyle:1` · [Civitai 688840](https://civitai.com/models/688840)
```text
A group of people standing outside a nightclub in the heart of a big city, neon signs flashing above. Some are talking, others checking their phones, and a bouncer watches over the entrance with a stern expression. The street is alive with activity and energy.  <lora:aidmaGTA5Style:1> <lora:aidmaInkStyle:1> dripping paint
```

**P122. Шоссе на закате, мост** – Flux.1 Dev + Castor-Gta6-Theme LoRA · [Hugging Face, prithivMLmods](https://huggingface.co/prithivMLmods/Castor-Gta6-Theme-Flux-LoRA)
```text
World of GTA 6, Captured at eye-level on a high-angle shot of a highway at sunset. The sky is a vibrant pink, with a few wispy clouds scattered across the sky. The sun is setting, casting a warm glow over the scene. In the foreground, a bridge stretches over a body of water, dotted with trees and a few cars. The bridge is adorned with a white truck with a red sign on the side, adding a pop of color to the scene to the image, GTA 6 Theme
```
Мост над водой на закате = Коммунальный / Бугринский мост через Обь – прямой аналог.

**P123. Вечеринка на крыше** – Flux.1 Dev + `gta6style` (Wiro AI) · [Hugging Face, WiroAI](https://huggingface.co/WiroAI/GTA6-style-flux-lora)
```text
[trigger], a rooftop party with neon lights, a pool, and city views. Stylish characters dance and socialize as a DJ plays, with the sunset sky glowing in the background.
```
`[trigger]` = `gta6style`.

**P124–P128. Pixpretty: город и настроение (5)** – ChatGPT, Gemini · [Pixpretty](https://pixpretty.tenorshare.ai/ai-insights/gta-style-ai-prompt.html)
```text
Neon-lit downtown at night with wet streets reflecting colorful signs, a GTA-inspired look.
```
```text
Gritty urban scene with deep blues and vibrant oranges in the Los Santos skyline, GTA Vice City style.
```
```text
Vinewood Hills at golden hour with dramatic lighting and a cinematic GTA V feel.
```
```text
Vast desert landscape under harsh sunlight, desolate and atmospheric in GTA V style.
```
```text
Beach chase scene with a character on a jet ski, summer vibes, stylized GTA look.
```

**P129–P131. Pixpretty: эпохи серии (3)** – [Pixpretty](https://pixpretty.tenorshare.ai/ai-insights/gta-style-ai-prompt.html)
```text
GTA Vice City style with 1980s neon colors, magenta and cyan lighting, art deco buildings, and pastel suits.
```
```text
GTA San Andreas vibe with early 90s hip-hop fashion, lowriders, graffiti, and warm haze.
```
```text
GTA 6-inspired concept with ultra-realistic graphics, detailed water physics, and a modern Vice City look.
```
Эпоха = палитра: Vice City – маджента и циан, San Andreas – тёплая дымка, IV – холодный серо-голубой (P047), VI – бирюза-коралл.

---

## 5. Интерфейс: «Mission Passed», звёзды розыска, мини-карта, меню, «скриншот игры»

Отдельного промта именно под надпись «Mission Passed» в открытом доступе нет: Lorka показывает картинку под заголовком «Mission passed! Respect +99» (`img/prompt-04-lorka-mission-passed.webp`), но сам промт не публикует. Ниже – промты, где HUD (интерфейс поверх кадра) прописан словами.

**P132. Скриншот игры с HUD (Postium, промт 3)** – модель не указана · [Postium](https://postium.ru/promt-dlya-foto-v-stile-gta-6/)
```text
Convert the uploaded photo into a realistic gameplay screenshot from a GTA VI-style open-world game. This must look like a normal in-game frame captured during gameplay, not a poster, not promotional art, not concept art, not a portrait and not a collage. Preserve the person’s facial likeness, body proportions, clothing identity and recognizable details. Render the person as a playable open-world game character inside the scene, with natural posture and believable interaction with the environment. Place the character on a Vice City-inspired street at night after rain: wet asphalt, palm trees, Art Deco buildings, parked cars, traffic, pedestrians, neon shop signs, streetlights, beach-city humidity and distant police lights. The character should look like they are walking through the city during a mission or free roam. Use real-time AAA game graphics: game-engine skin shading, slightly simplified pores, natural eye reflections, detailed hair, sharp clothing textures, visible seams, folds, denim, leather, metal accessories, roughness, normal maps and specular highlights. Materials must look like in-game assets, not a retouched photo. Add a clean GTA-style gameplay HUD: mini-map in the bottom-left corner, health and stamina bars, small mission objective, wanted stars, money counter, weapon icon and subtle interaction hints. Keep the HUD sharp and readable, but do not cover the face. Camera: third-person gameplay view, natural player camera, slightly behind or near the character, normal field of view, no poster framing, no hero pose, no title text, no logo, no graphic decorations. Lighting: believable in-game night lighting with neon reflections on wet streets, soft streetlight shadows, light atmospheric haze and natural city contrast.
```
Лучший разбор HUD по углам: мини-карта – низ слева, полоски здоровья, задача миссии, звёзды розыска, деньги, иконка оружия. И главное – `do not cover the face`, `no title text, no logo`.

**P133. GTA-Style Beach Club Gameplay Screenshot** – GPT Image 2 · [YouMind](https://youmind.com/prompts/gta-beach-club-gameplay-14400) · картинка: `img/prompt-15-youmind-beach-hud.webp`
```text
Create a hyper-realistic open-world crime video game screenshot in the style of a modern Miami-inspired beach club mission scene, captured in bright midday sunlight with a clear blue sky. Show a third-person gameplay-like composition with a young adult man with short dark hair, light skin, wearing a plain black t-shirt and patterned swim shorts seated casually in the foreground on pale sand, turned slightly to the side as if the player camera stopped near him. Place him large in frame, off-center left, with natural relaxed body posture. Behind him, depict an upscale beachfront club with exactly 3 white cabanas with flowing curtains visible across the sand, multiple tall palm trees, turquoise ocean water on the left, and an art-deco hotel strip on the right with pastel facades and neon accents. Populate the beach with a lively crowd of exactly 12 background people in swimwear: some standing and chatting, some walking near the shoreline, and exactly 2 seated at a dining table on the right with food and drinks. Include white lounge furniture, umbrellas, and a polished social party atmosphere. Add a convincing video game HUD overlay: a square mini-map in the bottom-left labeled GPS Route, weapon and control icons in the bottom-right, and a money counter in the top-right reading $45,670. The overall feel should resemble a next-gen Grand Theft Auto VI gameplay screenshot, cinematic but clearly in-game, with sharp environmental detail, realistic shadows, vibrant coastal color grading, and subtle satirical luxury-beach energy in Vice City.
```
Приём «exactly 3 / exactly 12 / exactly 2» – GPT Image 2 держит счёт объектов.

**P134. Video Game Screenshot Mockup Tropical Town (с переменными)** – GPT Image 2 (источник: Awesome GPT-Image-2, MIT) · [God of Prompt](https://godofprompt.ai/prompt-library/video-game-screenshot-mockup-tropical-town)
```text
Create a photorealistic third-person video game screenshot in the style of modern open-world action games (GTA, Red Dead Redemption). Over-the-shoulder perspective showing a male protagonist from behind wearing a grey tank top with "{{shirt-text}}" printed on the back and camouflage cargo shorts.
Setting: Sun-drenched tropical coastal town on a dirt road under blue sky with scattered clouds. Cinematic depth of field with the character sharp in foreground.
Left side: Weathered wooden welcome sign reading "Welcome to {{location-name}} YOUR PARADISE" with a pink plastic flamingo at its base, lush tropical foliage, water tower visible in distance.
Center: Faded green building with hand-painted "FISH" sign and marlin graphic, secondary sign advertising "BAIT TACKLE ICE BEER WINE", 2-3 pedestrian NPCs walking naturally.
Right side: Two-story wooden structure labeled "Brian's Boat Works & Marina", glowing "Brian's Bar" neon sign, weathered pickup truck parked outside, jet skis mounted on trailer.
Overlay UI elements with video game HUD aesthetic:
- Top-left: Mission objective box with title "{{mission-objective}}" and subtitle "Raul has some work for you at his boatyard" in clean sans-serif font
- Top-right: Time display "13:47" with cash counter "$1,142" and pink palm tree icon
- Bottom-left: Circular minimap with purple border showing roads and waypoints, north indicator visible
- Below minimap: Location text "{{location-name}}" over "PALM ISLAND" in bold caps
- Bottom-right: Subtle watermark "GTA VI / PRE-ALPHA FOOTAGE" in small transparent text
Lighting: Strong afternoon sun creating realistic shadows, slight atmospheric haze, saturated tropical color palette. Maintain AAA game graphics quality with detailed textures and ambient occlusion.
```
Шаблон с переменными `{{...}}` – как раз наш формат. Водяной знак «GTA VI / PRE-ALPHA FOOTAGE» – выдача за официальный кадр, убрать.

**P135. Open-World Game Screenshot Mockup (JSON-версия того же)** – GPT Image 2 · [YouMind](https://youmind.com/prompts/open-world-game-screenshot-mockup-14273)
```text
{
 "type": "video game screenshot mockup",
 "perspective": "third-person over-the-shoulder",
 "character": {
 "description": "male protagonist seen from behind",
 "clothing": "grey tank top with graphic 'LEONIDA MARINE CENTER', camouflage cargo shorts"
 },
 "environment": {
 "setting": "tropical coastal town, dirt road, sunny daytime with scattered clouds",
 "left_side": "wooden welcome sign reading 'Welcome to LEONIDA KEYS YOUR PARADISE', pink plastic flamingo, tropical foliage, distant water tower",
 "center": "green building with 'FISH' sign and marlin graphic, sign reading 'BAIT TACKLE ICE BEER WINE', pedestrians walking",
 "right_side": "two-story wooden building 'Brian's Boat Works & Marina', 'Brian's Bar' neon sign, parked pickup truck, jet skis on a trailer"
 },
 "ui_elements": {
 "count": 5,
 "components": [
 {
 "position": "top-left",
 "type": "mission objective",
 "text": "MEET RAUL\nRaul has some work for you at his boatyard"
 },
 {
 "position": "top-right",
 "type": "status HUD",
 "text": "13:47\n$1,142",
 "icon": "pink palm tree"
 },
 {
 "position": "bottom-left",
 "type": "minimap",
 "description": "circular map with purple border, white map icons including 'N' for north"
 },
 {
 "position": "bottom-left, right of minimap",
 "type": "location text",
 "text": "LEONIDA KEYS\nPALM ISLAND"
 },
 {
 "position": "bottom-right",
 "type": "watermark",
 "text": "GTA VI\nPRE-ALPHA FOOTAGE"
 }
 ]
 }
}
```

**P136. GTA-Style Dialogue Screenshot (меню выбора реплик)** – GPT Image 2 · [YouMind](https://youmind.com/prompts/gta-style-dialogue-screenshot-13890) **(анти-пример: чужой персонаж)**
```text
{
 "type": "video game screenshot",
 "style": "Grand Theft Auto VI aesthetic, realistic 3D graphics",
 "setting": "balcony overlooking a coastal city at sunset, palm trees, skyscrapers, warm lighting",
 "characters": [
 {
 "role": "NPC",
 "description": "Omni-Man, muscular older man with a mustache and grey temples, wearing a red and white superhero suit",
 "position": "center-left, facing camera"
 },
 {
 "role": "Player",
 "description": "man wearing a backwards dark baseball cap and light grey t-shirt",
 "position": "right foreground, back to camera"
 }
 ],
 "ui_elements": {
 "type": "dialogue menu",
 "position": "bottom center",
 "speaker_name": "OMNI-MAN",
 "dialogue_text": "This planet isn't yours to protect. Viltrumite rule is inevitable.",
 "choices_count": 3,
 "choices": [
 "1. You're not taking over anything.",
 "2. What do you want from me?",
 "3. I don't care about your politics."
 ],
 "highlight": "Choice 1 has a translucent purple background bar"
 }
}
```
Формат «диалог с выбором ответа» – отличная механика для карусели: «Клиент: магнитола не видит камеру. 1) Перепрошить 2) Поменять кабель 3) Ехать к нам». Персонажа заменить на своего мастера.

**P137. Главное меню игры с вашим лицом (Gemini)** – Gemini (Nano Banana), дальше видео в Google Flow / Veo 3 · [Ai Prompts and Tips, 13.05.2026](https://aipromptsandtips21.blogspot.com/2026/05/how-to-turn-yourself-into-gta-vi.html)
```text
Use the uploaded photo for exact same face reference and generate an ultra high-end AAA PC video game welcome screen inspired by the cinematic open-world atmosphere, neon-soaked nightlife, luxury crime-world energy, and ultra-realistic visual style of Grand Theft Auto VI while keeping the character fully original.
Keep the character exactly the same:
young male protagonist with accurate face identity from uploaded image, transformed completely into the same GTA-style semi-realistic game-art rendering as the environment and interface so the face naturally blends into the game graphics instead of looking like a pasted real photo.
Keep the outfit exactly the same:
slightly oversized white tropical open shirt with subtle floral texture, fitted black inner tank top, loose beige cargo pants with realistic folds, white sneakers, silver chain, black luxury wristwatch, black sunglasses resting slightly lower on nose.
Keep the pose exactly the same:
standing beside a luxury sports car, left hand resting on car roof, right hand inside pocket, body angled 35 degrees, relaxed confident posture, head slightly tilted toward camera.
Keep the environment exactly the same:
large Vice City-inspired neon urban street with palm trees, glowing hotel signs, wet reflective roads, luxury nightlife atmosphere, distant traffic, beach-city skyline, ambient smoke, cinematic environmental depth.
Keep the camera exactly the same:
horizontal 16:9 framing, cinematic wide shot, slightly low-angle perspective.
Keep the gameplay UI exactly the same:
STORY MODE
ONLINE
CONTINUE
SETTINGS
EXIT
PRO ADD-ON:
Ultra high detail, 8K resolution, AAA game-art rendering, cinematic color grading, volumetric lighting, neon reflections, wet surface reflections, HDR, global illumination, ambient occlusion, realistic fabric simulation, atmospheric depth, sharp UI integration.
```
Полезная фраза: `transformed completely into the same ... rendering as the environment ... instead of looking like a pasted real photo` – лечит «вклеенное лицо». Меню под сервис: «ЗАПИСАТЬСЯ / ЦЕНЫ / РАБОТЫ / КОНТАКТЫ» (текст лучше наложить потом).

**P138. Wanted-Star Mugshot Panel (звёзды розыска)** – ChatGPT · [Techpresso](https://academy.techpresso.co/prompts/chatgpt-prompts-gta)
```text
Reimagine [YOUR PHOTO] as a satirical wanted-poster loading panel in a gritty cel-shaded video-game style. Keep my face recognizable with a smirking deadpan expression, rendered in thick ink outlines and flat saturated tones over a worn paper texture. Add a row of bold cartoon stars across the top, a faux height chart behind me, and grimy edge wear. Bold poster cropping, satirical urban humor, high contrast, 4:5 portrait.
```
Совет автора: `three stars lit` – сколько звёзд горит. Для сервиса – шутка «Разыскивается: машина, которая не заводится в −35» со звёздами вверху.

**P139. Open-World Map Marker (экран карты)** – ChatGPT · [Techpresso](https://academy.techpresso.co/prompts/chatgpt-prompts-gta)
```text
Reimagine [YOUR PHOTO] as a stylized open-world map screen in a satirical cel-shaded game style. Keep my likeness recognizable in a circular player-icon portrait in the corner, with thick outlines and flat saturated color. Fill the rest with a flat illustrated city map: roads, a coastline, district blocks, and a glowing waypoint marker. Clean game-UI composition, bold HUD framing, high contrast, 16:9 landscape.
```
Совет автора: `a mock health and money bar in the HUD`. Для сервиса: «как к нам проехать» – стилизованная карта района с меткой бокса.

**P140. Пауза в действии + UI (Pixpretty)** – [Pixpretty](https://pixpretty.tenorshare.ai/ai-insights/gta-style-ai-prompt.html)
```text
GTA V loading-screen-style art with a paused action moment and subtle UI overlay.
```

**P141. GTA 6 в баре Синдзюку (короткий промт-переменная)** – GPT Image 2 · [Carat, prompt 622](https://carat.im/en/prompt-gallery/p/622), [YouMind](https://youmind.com/prompts/gta-6-shinjuku-bar-scene-15956)
```text
{argument name="game" default="GTA 6"} in {argument name="bar name" default="La Jetée Bar"} (that pays homage to Chris Marker) in {argument name="location" default="Shinjuku, Tokyo"}
```
**P142. GTA 6 на цветочном рынке Бангалора** – GPT Image 2 · [Carat, prompt 541](https://carat.im/en/prompt-gallery/p/541)
```text
{argument name="game" default="gta 6"} in {argument name="location" default="Bangalore’s market flower"} in India
```
Минимальный формат «игра + реальное место» – GPT Image 2 сам достраивает кадр игры. Аналог для нас: «game screenshot in a Novosibirsk car service bay in winter» – но без названия игры в итоговом посте.

**P143. Game Loading Screen (интерфейс загрузки, без GTA)** – GPT Image 2 · [Carat, prompt 24973](https://carat.im/en/prompt-gallery/p/24973)
```text
A stylish game loading screen interface design, dark futuristic background with glowing neon blue and orange accents, progress bar at the bottom, fantasy landscape artwork in the center panel, epic atmosphere with particle effects, AAA game UI aesthetic. No text, no watermark.
```
Элемент «полоса загрузки внизу» – на слайд «Загрузка… прошивка магнитолы 87%».

---

## 6. Постер и реклама бизнеса в стиле GTA

**P144. Сатирический билборд выдуманного продукта** – Flux.1 Dev + `aidmaGTA6` + `aidmaHyperrealism` · [Civitai 688840](https://civitai.com/models/688840) · картинка: `img/prompt-08-civitai-billboard.webp`
```text
A satirical billboard towering over a busy street, advertising a fictional product like "Crime Spree Energy Drink" with the slogan "Fuel Your Chaos - Coming Soon" in bright, exaggerated colors, poking fun at consumerism and pop culture.
,aidmaHyperrealism, aidmaGTA6
```
Сатирическая реклама выдуманных брендов – фирменный приём серии. Для сервиса: билборд над заснеженной улицей «Аккумулятор не боится −40». Текст читается (короткий, латиница); для кириллицы – накладывать отдельно.

**P145. Эпичный игровой постер с текстом (пародия на название)** – Flux.1 Dev + `aidmaGTA6` + `aidmatextimrover` · [Civitai 688840](https://civitai.com/models/688840) **(риск: пародия на товарный знак)**
```text
Epic Game Poster with a grandmother knitting and the Text:"GRANNY THEFT AUTO"      , aidmaGTA6, aidmatextimrover
```

**P146. Постер с текстом из облаков** – та же связка · [Civitai 688840](https://civitai.com/models/688840)
```text
Epic Game Poster with a stunning police chase and the Text:"GRAND THEFT LORA" made out of clouds     , aidmaGTA6, aidmatextimrover
```
Игра слов на «Grand Theft …» узнаётся мгновенно, но для бизнеса это заход на чужой знак – не используем.

**P147. Сатирический выпуск новостей на экране ТВ** – Flux.1 Dev + `aidmaGTA6` + `aidmaHyperrealism` · [Civitai 688840](https://civitai.com/models/688840)
```text
A satirical news broadcast on a television screen, reporting on absurd events in the city, with a newscaster delivering lines with a straight face.
,aidmaHyperrealism, aidmaGTA6
```
Формат «Новости Новосибирска: −38, город не завёлся» – слайд с юмором.

**P148–P149. Pixpretty: сатира и лайфстайл** – [Pixpretty](https://pixpretty.tenorshare.ai/ai-insights/gta-style-ai-prompt.html)
```text
Satirical in-game billboard ad for a fake product, parody style, on a city street, GTA 6-style.
```
```text
Luxury satire scene: a character in a designer hoodie and heels, surrounded by money and props, in a wild west setting, GTA 5 style.
```

**P150. Cel-Shaded Graffiti Mural (свой тег на стене)** – ChatGPT · [Techpresso](https://academy.techpresso.co/prompts/chatgpt-prompts-gta)
```text
Transform [YOUR PHOTO] into a street-art graffiti mural in a bold cel-shaded satirical style. Keep my likeness recognizable, painted large across a weathered brick wall with thick spray-can outlines, vivid flat fills, drips, and a stenciled tag beside me. Rough concrete texture, harsh urban daylight, and a chain-link fence in the foreground. Gritty graphic poster composition, high contrast, 4:5 portrait.
```
Совет автора: `beside me reads ACE` – текст тега в кавычках.

**P151. Viral Reels Cover Style** – ChatGPT · [Media.io](https://www.media.io/image-effects/chatgpt-gta-style-poster-prompts.html)
```text
Design a viral Instagram Reels cover in GTA VI art style with cinematic portrait framing and bold lighting contrast. Establish luxury tropical city vibe through strong graphical composition using pink-orange neon palette. Deliver modern game marketing artwork aesthetic with ultra sharp details that stop scrolling feeds and drives engagement across social media platforms.
```

**P152–P153. Pixpretty: постер для группы** – [Pixpretty](https://pixpretty.tenorshare.ai/ai-insights/gta-style-ai-prompt.html)
```text
Gaming poster: a group photo turned into an epic GTA-style poster for a gaming room.
```
```text
A heist crew lineup of four unique characters in tactical gear inside a rundown safehouse, each with a distinct story, GTA-style.
```

Плюс уже выше: P064 (персонаж + крупная жёлтая надпись за головой), P106 (ровно 2 текстовых элемента), P067 (наклейка с ценой), P082 (мастер на плоском фоне) – всё это рекламные раскладки.

---

## 7. Негативные промты, параметры, LoRA и веса

### 7.1. Промты-образцы для Flux / SDXL / SD 1.5 (из карточек LoRA)

**P154. Чистое описание стиля** – [Pixpretty](https://pixpretty.tenorshare.ai/ai-insights/gta-style-ai-prompt.html)
```text
Cel-shaded scene with sharp contrast, bold black outlines, and flat colors.
```

**P155. Крупный план женщины (gta6style)** – Flux.1 Dev + LoRA WiroAI `gta6style` · [Hugging Face, WiroAI](https://huggingface.co/WiroAI/GTA6-style-flux-lora)
```text
[trigger], a cinematic close-up of a young woman with a determined yet emotional expression, her face illuminated by a warm, dim light. She has subtle freckles, hoop earrings, and a loose braid resting on her shoulder. The background is softly blurred, hinting at a modest room with a glowing bedside lamp, adding depth and a sense of intimacy to the scene.
```

**P156. Тропические горы (Castor)** – Flux.1 Dev + Castor LoRA · [Hugging Face](https://huggingface.co/prithivMLmods/Castor-Gta6-Theme-Flux-LoRA)
```text
GTA 6 Theme, World of GTA 6, (Masterpiece, best quality:1.2), (Masterpiece, best quality:1.2), landscape, perspective aerial view, tropical mountains, landscape indigo accent, mythology, cinematic, detailed, atmospheric, backlit, epic, cinematic, understanding art, matte painting, beautiful scenery, Realistic lighting, Masterpiece, Good quality, Nice graphics, High level of detail, ultra detailed, cinematic lighting, HDR, Illustration, --v6
```
`--v6` – параметр Midjourney, во Flux ничего не делает. Мусор, перенесённый «по привычке».

**P157. Разрушенный город (Castor)** – Flux.1 Dev + Castor LoRA · [Hugging Face](https://huggingface.co/prithivMLmods/Castor-Gta6-Theme-Flux-LoRA)
```text
 GTA 6 Theme, World of GTA 6, Crumbling City, unreal engine, greg rutkowski, loish, rhads, beeple, makoto shinkai and lois van baarle, ilya kuvshinov, rossdraws, tom bagshaw, alphonse mucha, global illumination, detailed and intricate environment
```
Список живых художников – так делать не надо (этика и права авторов).

**P158. Мужчина в костюме (Pegasi, SDXL)** – SDXL + Pegasi-Beta-GTA-LoRA (база RealVisXL V4.0 или SDXL base) · [Hugging Face, prithivMLmods](https://huggingface.co/prithivMLmods/Pegasi-Beta-GTA-LoRA)
```text
A picture in the style of a gta 5 poster game, GTA V,  Grand Theft Auto 5 poster,  16k, UHD, HDR, solo human, a blond man with a beard and glasses, in a formal suit
```

**P159. Реальный музыкант (Pegasi)** – SDXL · [Hugging Face](https://huggingface.co/prithivMLmods/Pegasi-Beta-GTA-LoRA) **(анти-пример: реальный человек)**
```text
A picture in the style of a gta 5 poster game, GTA V,  Grand Theft Auto 5 poster,  16k, UHD, HDR, Liam Gallagher, moody, wearing a fishtail parka 
```

**P160. Киногерой в San Andreas (Pegasi)** – SDXL, сэмплер euler · [Hugging Face](https://huggingface.co/prithivMLmods/Pegasi-Beta-GTA-LoRA) **(анти-пример: чужой персонаж)**
```text
John Wick as a GTA San Andreas cartoon, John Wick imagined as a cartoon drawing from Grand Theft Auto
```

**P161. GTA5 Artwork Diffusion (Dreambooth, SD 1.5)** – SD 1.5, Guidance 7, 65 шагов DDIM · [Hugging Face, ItsJayQz](https://huggingface.co/ItsJayQz/GTA5_Artwork_Diffusion)
```text
*name* in gtav style
```
Модель обучена на загрузочных экранах и артах GTA Online; лицензия CreativeML OpenRAIL-M, автор прямо пишет – не для коммерции.

**P162. Flux GTA6 (Motas)** – Flux.1 Dev + `aidmaGTA6` · [Hugging Face, Motas](https://huggingface.co/Motas/GTA6) **(анти-пример: чужой персонаж)**
```text
spiderman wearing a tutu dancing ballet in the middle of an urban street, next to him a smiling police officer clapping, aidmaGTA6, traffic jam behind them depth of field background  <lora:aidmaGTA6:1>
```

**P163–P164. FounderFeed gta-style-lora** – Flux.1 Dev, триггер `aidmaGTA5`, лицензия MIT · [Hugging Face, FounderFeed](https://huggingface.co/FounderFeed/gta-style-lora)
```text
aidmaGTA5 style man
```
```text
A night Scenes of Gta v
```

**P165. Кот с сигарой на балконе («GTA 6 style:»)** – Flux.1 Dev + LoRA «GTA 6 Style – Wallpaper / Loading Screen», 22 шага, CFG 1.5, Euler, 1080×1080 · [Civitai, модель 1551916](https://civitai.com/models/1551916)
```text
GTA 6 style: cat, the cat is holding a cigar, it's looking at the city from a white balcony. Behind him, palm trees sway in the breeze and the swimming pool below reflects the glow of neon lights. The sky is deep indigo, with a helicopter circling far overhead. The mood is rich with arrogance, danger, and the quiet high of a man who’s taken everything — and knows it can all go in a flash.
```

**P166. Пейзаж Юпитера «Gta V loading screen style»** – SDXL + LoRA «GTA V loading screen artstyle» (триггер `gtv style`), 25 шагов, CFG 4, DPM++ 2M Karras · [Civitai, модель 119307](https://civitai.com/models/119307)
```text
Jupiter landscape. Alienworld. Colorful. Cats roaming around. Gta V loading screen style.
```
Негатив: `boring, worst quality, thumbnail,`

**P167. GTA IV Loading Screen Art (SDXL)** – SDXL + LoRA, триггер `gr4nd_th3ft_4` · [Civitai, модель 525897](https://civitai.com/models/525897)
```text
gr4nd_th3ft_4
```
Настройки автора: чекпойнт jibMixRealisticXL, 25 шагов (рефайнер с 20), CFG 3, UNI_PC + SGM (или DPMPP_2M_SDE + Karras), 1024×768. Стиль GTA IV – холодный, контрастный, ближе всего к зиме.

**P168. Синтаксис веса LoRA в промте (A1111 / Forge)** – Flux + `Grand Theft Auto VI Style:0.75` · [Civitai 688840](https://civitai.com/models/688840) **(в кадре оружие – только как пример синтаксиса)**
```text
Avant-garde anime-inspired illustration, cinematic tense urban standoff at night. Close-up on a rugged man with sharp features and stubble, intense gaze, aiming a handgun directly at the viewer. Sun-kissed skin, visible forehead wrinkle, slicked-back brown hair, brown-red gradient aviator sunglasses reflecting city lights. Rolled-up white shirt, black tactical vest, black leather gloves, detailed wristwatch, tattooed forearm. Dramatic blue and red police lights illuminating his face and gear. Police cars with flashing lights behind him, blurred city street, neon-lit signs, warm orange streetlights, and distant crowds. Graphic-novel style, high detail, bold outlines, dynamic composition, shallow depth of field, stylized bloom and ambient occlusion, Unreal Engine + anime hybrid, moody color grading, extreme closeup, filmic widescreen aspect. <lora:Grand Theft Auto VI Style:0.75><segment:Anzhc-Face-Seg-1024-v2-y8n.pt,0.4,0.5//cid=1> <segment:Ryzo-Hand-Seg-1024-v2-y8m.pt,0.4,0.5//cid=1
```
`<segment:...>` – доработка лица и рук детектором (ADetailer-подобно) – полезно, когда лицо мастера «плывёт».

### 7.2. Негативные промты (дословно)

| № | Где | Негатив | Комментарий |
|---|---|---|---|
| N1 | SDXL, «GTA V loading screen» (Civitai 119307, `gtv style`) | `text, watermark, (bad art), (deformed), (poorly drawn), strange colours, multiple hands, multiple fingers, disfigured` | короткий рабочий – берём за основу |
| N2 | там же, Юпитер | `boring, worst quality, thumbnail,` | минимальный |
| N3 | SDXL, Civitai 558832 (`drawing gta style v2`) | `ugly, deformed, noisy, blurry, low contrast, realistic` | `realistic` в негативе – держит рисунок |
| N4 | Z-Image, Civitai 558832 (cinematic-версия) | `anime, cartoon, graphic, text, painting, crayon, graphite, abstract, glitch, deformed, mutated, ugly, disfigured, painting, drawing, illustration, glitch, deformed, mutated, cross-eyed, ugly, disfigured, painting, drawing, illustration, glitch, deformed, mutated, cross-eyed, ugly, disfigured, anime, cartoon, graphic, text, painting, crayon, graphite, abstract, glitch, deformed, mutated, ugly, disfigured, anime, cartoon, graphic, text, painting, crayon, graphite, abstract, glitch, deformed, mutated, ugly, disfigured` | **наоборот** – запрещает рисунок, для «кинокадра»; для нашего стиля не брать |
| N5 | SDXL, P091 (Civitai 119307) | `NEGATIVE_HANDS, nudity, genitals, nipples, NSFW, Cleavage, Pubic Hair, Nudity, Naked, Au naturel, Watermark, Text, censored, deformed, bad anatomy, disfigured, poorly drawn face, mutated, extra limb, ugly, poorly drawn hands, missing limb, floating limbs, disconnected limbs, disconnected head, malformed hands, long neck, mutated hands and fingers, bad hands, missing fingers, cropped, worst quality, low quality, mutation, poorly drawn, huge calf, bad hands, fused hand, missing hand, disappearing arms, disappearing thigh, disappearing calf, disappearing legs, missing fingers, fused fingers, abnormal eye proportion, Abnormal hands, abnormal legs, abnormal feet,  abnormal fingers` | длинный «от рук», `NEGATIVE_HANDS` – эмбеддинг |
| N6 | GPT Image 2, P072 | `NEGATIVE: real humans, photoreal poster, movie poster style, flat illustration only` | негатив внутри текста – так в GPT |
| N7 | ChatGPT, P071 | `Avoid photorealistic live-action, anime, flat vector icons, retro film look, toy/chibi style.` | лучший короткий для ChatGPT |
| N8 | ChatGPT, P079 | `No text, logos, watermark, game HUD or additional people.` | обязательный хвост для бизнеса |
| N9 | GPT Image 2, P015 | `Do not include: camera equipment, gimbal, audiovisual gear, real logos, text, trademarks, weapons, facial deformities, poorly constructed hands, excessive muscle mass, cartoonish appearance, or costume-like look.` | хорош `trademarks, weapons, costume-like look` |
| N10 | любой, P044–P049 | `Не генерируй: … фотореалистичную текстуру кожи, деформацию лица, лишние пальцы.` | русский формат антипромта |

### 7.3. Параметры Midjourney (что нашлось)

- `--ar 16:9 / 9:16 / 1:1` – из шаблона WildChat (P054–P057); для карусели нужен `--ar 4:5`.
- `--s 750 --v 5.2` – P118; `--s` (stylize) 250–750 = сильнее «художественность».
- `--ar 2:3 --quality 2 --style raw` – P072 (в GPT не работает). `--style raw` уменьшает «украшательство» Midjourney – для GTA-иллюстрации обычно не нужен.
- **Готового `--sref`-кода под GTA не нашлось** ни в Midlibrary, ни в sref-библиотеках. Рабочий путь: сделать 1–3 удачных кадра без логотипов и подавать их как `--sref <ссылка на картинку> --sw 100–300`.
- Классический хвост стиля для MJ (P050–P052, P061): `in the style of a grand theft auto, loading screens ,GTA style artwork highly detailed, celshading, digital painting style, dramatic composition, 21st century comic book cover, studio lighting`.
- В выдаче поиска встретился пересказ комментария на Lemmy: стиль загрузочных экранов описывают как смесь **Pop Art + Neo-noir**. Сам комментарий открыть не удалось – маркер не проверен.

### 7.4. LoRA и триггер-слова

| LoRA / модель | База | Триггер | Вес и настройки | Лицензия, заметки |
|---|---|---|---|---|
| [GTA VI Lora – GTA 6 + GTA V Style](https://civitai.com/models/688840) | Flux.1 Dev | `aidmaGTA6`, `aidmaGTA5` | 0.5–1.0; примеры: 30–35 шагов, CFG 3.5, Euler | 2 200 скачиваний – самая популярная |
| [GTA6 Style Flux LoRA (Wiro AI)](https://civitai.com/models/1111914) | Flux.1 Dev | `gta6style` | – | **flux-1-dev-non-commercial** – для рекламы нельзя |
| [GTA 6 Style – Wallpaper / Loading Screen](https://civitai.com/models/1551916) | Flux.1 Dev | `GTA 6 style:` | CFG 1.5–3.3, 22–30 шагов | глянцевый промо-стиль |
| [GTA Style (gt9style)](https://civitai.com/models/66719) | MOSS Image (в карточке) | `gt9style` | 0.6 | серия «персонаж на плоском фоне» (P082) |
| [GTA style zib / drawing gta style](https://civitai.com/models/558832) | SDXL, Flux, Z-Image | `cinematic`, `GTA style` | 0.8–1.0 | несколько версий в одной карточке |
| [GTA V loading screen artstyle](https://civitai.com/models/119307) | SDXL 1.0 | `gtv style` | CFG 4–8, 25–30 шагов | 3 000 скачиваний |
| [GTA IV Art (Colorful)](https://civitai.com/models/525897) | SDXL 1.0 | `gr4nd_th3ft_4` | CFG 3, 25 шагов, jibMixRealisticXL | холодная палитра |
| [GTA5 Artwork Diffusion](https://huggingface.co/ItsJayQz/GTA5_Artwork_Diffusion) | SD 1.5 (Dreambooth) | `gtav style` | Guidance 7, 65 шагов DDIM | автор: не для коммерции |
| [Pegasi-Beta-GTA-LoRA](https://huggingface.co/prithivMLmods/Pegasi-Beta-GTA-LoRA) | SDXL | `Gta` | Euler a | OpenRAIL-M |
| [Castor-Gta6-Theme](https://huggingface.co/prithivMLmods/Castor-Gta6-Theme-Flux-LoRA) | Flux.1 Dev | `GTA 6 Theme`, `World of GTA 6` | – | автор: «в обучении, возможны артефакты» |
| [FounderFeed gta-style-lora](https://huggingface.co/FounderFeed/gta-style-lora) | Flux.1 Dev | `aidmaGTA5` | 1 000 шагов обучения | MIT |
| Ещё в поиске Civitai | Krea 2, Qwen, Z-Image, Illustrious, Pony, NoobAI, Wan 2.2 (видео) | `GTA_SA_Style`, `gtaillvi`, `gta-gloss-style`, `GTA_Style,`, `pkgta6`, `xgtasax` и др. | – | ~40 моделей по запросу «GTA style» |
| [Lucia Caminos (GTA VI)](https://civitai.com/models/2906696) | Krea 2 | `lccmns` | – | **персонаж игры – не использовать никогда** |

---

## 8. Разбор: из чего состоит рабочий промт

Сравнил 168 промтов. Те, у которых картинка-результат похожа на «загрузочный экран», содержат 8 блоков в таком порядке:

| # | Блок | Зачем | Пример из лучших промтов |
|---|---|---|---|
| 1 | **Задача** | перерисовать фото или новая сцена | `Transform the uploaded photo into ...` / `Create a ...` |
| 2 | **Что сохранить** | лицо, одежда, поза, машина | `Preserve the person’s recognizable face, hairstyle, skin tone, build and outfit` (P079) |
| 3 | **Кто и что делает** | одно действие, одна поза | `relaxed, confident three-quarter pose beside a parked sports car` |
| 4 | **Где** | фон, детали места | `palm-lined coastal boulevard ... pastel art-deco buildings` |
| 5 | **Техника рисунка** | это и есть «GTA» | `bold black contours, semi-realistic facial details, cel-shaded colors and hard-edged shadows` |
| 6 | **Палитра и свет** | эпоха серии | `coral, magenta and turquoise accents`, `pink-orange sunset`, `neon rim light` |
| 7 | **Композиция и формат** | постерность | `low-angle`, `knees up`, `person as the focal point`, `vertical 9:16` / `4:5` |
| 8 | **Запреты** | права и мусор | `No text, logos, watermark, game HUD or additional people` |

Короткие промты (P004, P021, P102) тоже работают, но только в моделях, где GTA-стиль «вшит» (ChatGPT, DALL-E, LoRA). Промты без блока 5 (Magica, P111–P112) стиля не дают вообще.

### 8.1. Две раскладки, которые узнаются сразу

1. **Персонаж на плоском фоне.** Человек по пояс или в рост, фон – один насыщенный цвет (горчичный, оранжевый, красный, бирюзовый) с тёмными силуэтами по теме. Это раскладка загрузочных экранов GTA V (P082, P083, P064, P054–P057 – `flat backgrounds`).
2. **Сетка панелей с чёрными рамками.** 3×3, 2×3 или «центральный портрет + мозаика вокруг» (P065, P066, P067, P072, P073–P076).

Третья, отдельная – **«скриншот игры с HUD»** (P132, P133, P134): мини-карта, звёзды, деньги, задача миссии.

## 9. Слова, которые дают стиль, и слова, которые его ломают

### 9.1. Дают узнаваемый стиль

- Техника: `thick black outlines`, `bold black ink contours`, `cel-shaded` / `celshading`, `flat saturated color blocks`, `hard cartoon shadows`, `halftone grit`, `comic-grit texture`, `painterly digital illustration`, `digital painting style`, `glossy poster finish`.
- Лицо: `semi-realistic painted face`, `realistic but stylized face, clean jawline, angular features, crisp eyebrows, reduced skin microdetail`.
- Жанр кадра: `loading-screen illustration`, `game key art`, `box-art collage`, `21st century comic book cover`, `satirical urban poster`, `Pop Art + Neo-noir`.
- Композиция: `low-angle hero shot`, `poster cropping`, `three-quarter pose`, `solid [color] background with silhouettes of ...`, `3x3 grid with thick black dividers`.
- Палитра по эпохам: Vice City – `magenta, cyan, pastel`; GTA VI – `coral, magenta, turquoise, gold highlights, near-black shadows`; San Andreas – `warm orange haze`; GTA IV – `cold grey-blue, muted yellow`; GTA V – `deep blues and vibrant oranges`.
- Свет: `neon rim light`, `pink-orange sunset`, `hard directional sunlight`, `wet asphalt reflecting the neon`.

### 9.2. Ломают стиль или создают риск

| Слово / приём | Что происходит | Доказательство |
|---|---|---|
| `ultra-realistic`, `photograph`, `hyperrealism`, `8K photo`, `realistic art style` | получается фото, рисунок исчезает | картинки №06, 07, 08, 16 |
| `official`, `Rockstar promotional`, `title “Grand Theft Auto VI”`, `Add GTA 6 Logo` | рисует логотип GTA VI, значок R, иногда рейтинг ESRB | картинки №12, 13 |
| имена (`Tommy`, `Lance`, `Jason`, `Lucia`, знаменитости) | копия чужого персонажа / лица | P072, P076, P159 |
| «типаж 80-х Майами» без своего фото | лицо похоже на известного актёра | картинка №14 |
| группа больше 4 человек | лица теряют сходство | Techpresso, Lorka |
| длинный «суп» из противоречий (`Add GTA 6 Logo` + `no real logos`) | модель выбирает случайно | P015 |
| текст на русском, длинные слоганы, номера машин | каша из букв | общий опыт генераторов; Ideogram и GPT Image держат только короткую латиницу в кавычках |
| `--v6`, `--ar` в ChatGPT / Flux | не работает, просто мусор | P156, P072 |
| сюжет без техники рисунка (`A stolen car being dismantled ...`) | обычная картинка без GTA | P111–P112 |
| пальмы, пляж, Майами по умолчанию | зима «съедается» тропиками | P045, P046, P048: «Не генерируй: зимний пейзаж» |
| оружие, наркотики, угон, полиция | модерация соцсетей, отказ модели; для сервиса – антиреклама | P007, P039, P088, картинка №04 |

## 10. Чем промт для ChatGPT отличается от Midjourney и остальных

| | ChatGPT / gpt-image / GPT Image 2 | Nano Banana / Gemini | Midjourney | Flux / SDXL (LoRA) | Ideogram | Leonardo |
|---|---|---|---|---|---|---|
| Язык промта | связный абзац, можно JSON | связный абзац; любит «Keep … exactly the same» | короткие токены через запятую + хвост стиля | токены + триггер LoRA | 2–3 предложения | как MJ |
| Фото-референс | да, лицо держит хорошо | да, лучше всех по коже и свету (по Postium) | `--oref` / `--cref` по ссылке | IP-Adapter / PuLID, отдельно | style reference до 3 картинок | Image Guidance |
| Как задать стиль | словами техники (блок 5) | словами техники | хвост стиля + `--s` + `--sref` | триггер LoRA (`aidmaGTA6`) с весом 0.5–1.0 | словами + style reference | Style Reference |
| Негатив | внутри текста: `Avoid …`, `No text, logos …` | внутри текста | `--no text, logo, watermark` | отдельное поле negative (SDXL); у Flux CFG ≈1–3.5, негатив слабый | внутри текста | поле negative |
| Формат | словами: `vertical 4:5` или выбор в интерфейсе | словами | `--ar 4:5` | размер в пикселях (832×1216, 1080×1350) | выбор в интерфейсе | выбор |
| Текст в кадре | короткая латиница в кавычках, `exactly 2 text elements` | короткая латиница | слабо | слабо (нужна текстовая LoRA) | **лучше всех**: текст в кавычках рисуется буквально | средне |
| Доработка | диалогом: «сделай контур толще» | диалогом | вариации / ремикс | seed + inpaint | ремикс | – |
| Что нашли | ≈105 (+12 DALL-E) | 4 | 11 | ≈33 | **готовых GTA-промтов не нашли** | **готовых GTA-промтов не нашли** |

Практический вывод: основной инструмент – ChatGPT (gpt-image) или Nano Banana с фото мастера и машины клиента; Midjourney – для фонов и сцен без людей; Flux + `aidmaGTA6` – если нужен пакет из десятков однотипных кадров; Ideogram – если на картинке нужен короткий английский заголовок.

## 11. Права: как не нарушить

Не юридическое заключение; перед платной рекламой – прогнать через скилл `юр-проверка-сайта` или юриста.

**Что охраняется, а что нет**
- Стиль как таковой (толстый контур, cel-shading, закатная палитра) – не объект авторского права: охраняются конкретные произведения, а не идеи и приёмы (ст. 1259 ГК РФ).
- Охраняются: логотип и шрифтовое написание «Grand Theft Auto» / «GTA» / римская «VI», значок Rockstar «R» – товарные знаки (ст. 1477, 1484 ГК РФ); персонажи (Джейсон, Люсия, Томми, Си-Джей, Майкл и др.), конкретные обложки и арты – произведения (ст. 1259, 1270).
- Использование чужого знака в рекламе – недостоверная / недобросовестная реклама (ФЗ «О рекламе», ст. 5) и риск недобросовестной конкуренции через смешение (ФЗ «О защите конкуренции», ст. 14.6).
- Политика Rockstar / Take-Two разрешает фанатский контент только некоммерческий: не зарабатывать и не продвигать товары и услуги ([Rockstar Support](https://support.rockstargames.com/articles/200153756/Policy-on-posting-copyrighted-Rockstar-Games-material)). Пост автосервиса – это продвижение услуги.

**Правила для наших промтов**
1. Никогда не просить: логотип, название игры, значок R, рейтинг ESRB, «official», «Rockstar promotional», водяной знак «GTA VI footage».
2. Не называть и не описывать персонажей игры (Джейсон и Люсия, Томми Версетти и т.д.), не брать персонажные LoRA (Lucia `lccmns`), не загружать официальные арты как референс (P019–P020).
3. Не делать пародий на название («Grand Theft Service», «Granny Theft Auto») – это всё равно заход на знак.
4. Знаменитости и чужие лица – нет; только наши мастера и клиенты с их согласия (см. правило «лицо не трогать» – лицо держим по фото).
5. Внутри промта для модели слово `GTA-inspired` – допустимый указатель стиля (модель иначе не поймёт), но **в результате** не должно быть ни одного знака. Безопасная формулировка:
   - `in the style of 2000s–2020s open-world crime game loading-screen illustrations` – вообще без бренда;
   - `GTA-inspired illustration style (no logos, no game titles, no characters from any game)` – если без слова стиль не ловится.
6. В подписи поста не писать «в стиле GTA 6» как рекламный приём; нейтрально – «если бы наш бокс был игрой». Хештеги с названием игры для рекламного поста не ставить.
7. Каждую картинку проверять глазами на случайный логотип, значок R, надписи «Grand Theft Auto», знаки на машинах и номера (номера – всегда пустые или закрыты, правило Артёма).
8. LoRA с некоммерческой лицензией (Wiro `gta6style`, GTA5 Artwork Diffusion) – для рекламы не брать.

---

## 12. Пять базовых шаблонов под автосервис (без генерации, не проверены)

Переменные: `[car]` – марка, модель, цвет, год (например `white 2019 Toyota Land Cruiser Prado`); `[scene]` – что происходит; `[season]` – см. словарь сезона ниже. Текст на русском в кадр не просим – ставим потом в Figma / Canva. Формат карусели – 4:5 (1080×1350); если модель даёт только 2:3, кадрировать.

**Словарь `[season]`** (вставлять целиком):
- зима: `deep Siberian winter: packed snow on the ground, frost on glass and metal, visible breath vapor, snowflakes in the light, low pink-orange winter sunset with long cold blue shadows, sodium-orange streetlights, no palm trees`
- весна: `early Siberian spring: melting dirty snow at the curbs, puddles reflecting a pastel sunset, wet asphalt, bare birch trees, no palm trees`
- лето: `short hot Siberian summer: warm golden evening light, dusty asphalt, green birches and poplars, haze over the city, no palm trees`
- осень: `Siberian autumn: yellow birch leaves on wet asphalt, grey-blue sky with an orange sunset break, first frost, no palm trees`

**Общий хвост для всех (запреты)**:
```text
No text, no letters, no logos, no game titles, no brand badges, no watermark, blank license plates, no weapons, no characters from any existing game, no celebrities.
```

### Ш1. Мастер в боксе – портрет «загрузочный экран» (фото мастера → ChatGPT / Nano Banana)

```text
Transform the uploaded photo of a car service technician into a loading-screen character illustration inspired by 2000s–2020s open-world crime game key art. Preserve his recognizable face, hairstyle, facial hair, skin tone, build and work clothes exactly; redraw the face as a semi-realistic painted face with a clean jawline, crisp eyebrows and reduced skin microdetail, so it blends with the illustration instead of looking like a pasted photo. Show him from the knees up in a confident three-quarter pose, [scene] (for example: holding a torque wrench over his shoulder next to [car] on a lift). Background: a solid saturated [mustard yellow / burnt orange / teal] color with dark flat silhouettes of a service bay, a car lift, tool chests and a garage door. Season mood: [season]. Technique: thick black ink outlines, cel-shaded flat color blocks, hard-edged shadows, subtle halftone grit, glossy poster finish. Palette: the background color plus coral, magenta and turquoise accents and deep near-black shadows. Low-angle poster composition, vertical 4:5, the technician is the focal point, empty space at the top for a headline. No text, no letters, no logos, no game titles, no brand badges, no watermark, blank license plates, no weapons, no characters from any existing game, no celebrities.
```
Собран из P082 (плоский фон + силуэты), P079 (порядок блоков), P071 (описание лица), P137 (`instead of looking like a pasted photo`).

### Ш2. Машина клиента – «геройский» кадр (фото машины или текст → любая модель)

```text
Front three-quarter low-angle view of [car] in the style of an open-world crime game loading-screen illustration, [scene] (for example: just leaving our service bay at dusk, headlights on). Setting: a Novosibirsk street with Soviet-era apartment blocks, a wide avenue and a river bridge in the distance. Season and light: [season]. Render the car accurately (body shape, headlights, wheels, color) as a cohesive digital illustration: bold black contours, cel-shaded paint with glossy highlights and neon rim light, hard shadows, painterly sky, light halftone grit. Palette: pink-orange sunset sky against cold blue shadows, warm orange streetlights, a touch of magenta and turquoise. Car large in frame, vertical 4:5, empty band at the bottom for a caption. No text, no letters, no logos, no game titles, no brand badges, no watermark, blank license plates, no weapons, no characters from any existing game, no celebrities.
```
Midjourney-вариант (без фото): `[car] leaving a car service at dusk, Novosibirsk street, [season], loading-screen illustration, thick black outlines, celshading, digital painting style, dramatic composition, comic book cover, pink-orange sky, cold blue shadows --ar 4:5 --s 400 --no text, logo, letters, watermark, license plate numbers`
Flux-вариант: в начало `aidmaGTA6,` (LoRA вес 0.7–0.9, CFG 3.5, 30 шагов, 1080×1350), слово `photograph` не писать.

### Ш3. Обложка карусели – сетка панелей (ChatGPT / GPT Image 2)

```text
Create a vertical 4:5 cover in the style of a classic open-world crime game box-art collage: a grid of 6 illustrated panels separated by thick black dividers, plus one empty horizontal title bar across the middle (leave it blank, solid dark color, for a headline added later). Panels: 1) top-left – close-up of [car] headlights with frost, [season]; 2) top-right – a technician's gloved hands connecting a diagnostic scanner under the hood; 3) middle-left – [scene]; 4) middle-right – a glowing car head unit screen in a dark cabin, generic interface without readable text; 5) bottom-left – the service bay at night with neon light strips and a car on a lift; 6) bottom-right – [car] driving away on a snowy Novosibirsk street at sunset. Technique: thick black ink outlines, cel-shaded flat colors, hard shadows, halftone grit, glossy finish; each panel has its own dynamic angle (low-angle cars, close-ups). Palette: coral, magenta, turquoise, warm orange streetlights, cold blue snow shadows. Clean separation between panels. No text, no letters, no logos, no game titles, no brand badges, no watermark, blank license plates, no weapons, no characters from any existing game, no celebrities.
```
Собран из P065, P072 (раскладка «позиция → содержание», `clean separation between panels`), P066.

### Ш4. Магнитола в салоне (фото салона или текст → ChatGPT / Nano Banana)

```text
Interior view from the passenger seat of [car], illustrated as an open-world crime game cutscene frame: a large glowing aftermarket Android head unit screen in the center console shows a generic navigation map with a glowing route (no readable text, no brand names), soft screen light on the dashboard and the driver's hands on the steering wheel. Through the windshield: [season], a Novosibirsk street at night with blurred traffic lights. [scene]. Technique: bold black contours, semi-realistic painted forms, cel-shaded surfaces, hard shadows, neon rim light from the screen, light halftone grit. Palette: deep night blue cabin, turquoise screen glow, warm orange streetlights, magenta accents. Cinematic composition, the screen as the focal point, vertical 4:5. No text, no letters, no logos, no game titles, no brand badges, no watermark, blank license plates, no weapons, no characters from any existing game, no celebrities.
```
Для реального фото салона добавить в начало: `Transform the uploaded photo, keep the exact dashboard shape, head unit size and position, and camera angle; do not add objects that are absent from the photo.` (приём из P011).

### Ш5. «Миссия выполнена» – кадр игры с интерфейсом (GPT Image 2 / ChatGPT)

```text
Create a third-person video game screenshot of an open-world crime game, not a poster. The player character, a car service technician in work clothes seen from behind, stands next to [car] in front of an open service bay gate; [scene]. Environment: [season], a Novosibirsk industrial street at dusk, snowbanks, steam from the bay, neon light strip above the gate. Add a clean game HUD with exactly 4 elements: 1) bottom-left – a circular minimap with roads and one glowing waypoint, no labels; 2) top-right – a row of 5 star icons; 3) top-left – an empty dark mission objective box with no text inside; 4) center – a large empty rounded banner for a completion message, no text inside. Keep the HUD sharp and do not cover the face or the car. Style: cel-shaded game graphics with bold outlines and slightly simplified textures, vibrant color grading, warm orange light from the bay against cold blue snow. Normal player camera, vertical 4:5. No text, no letters, no logos, no game titles, no brand badges, no watermark, blank license plates, no weapons, no characters from any existing game, no celebrities.
```
Собран из P132 (HUD по углам, `do not cover the face`), P106 (`exactly N elements`), P134 (переменные). Надпись «МИССИЯ ВЫПОЛНЕНА» и звёзды-оценку ставить в Figma – так текст будет чистым и по-русски.

### Как проверять шаблоны (когда дойдёт до генерации)
1. Прогнать каждый на 3–5 реальных фото (мастер, машина клиента, салон) – до этого шаблон «не проверен».
2. Чек-лист кадра: лицо похоже; есть толстый контур и cel-shading; нет логотипа, значка R, надписей, знаков на машине; номера пустые; нет пальм зимой; руки и пальцы целые.

---

## 13. Источники

Промты и картинки:
- [Techpresso – 30 ChatGPT GTA prompts](https://academy.techpresso.co/prompts/chatgpt-prompts-gta) (обновлено 27.10.2026)
- [Postium – промт для фото в стиле GTA 6](https://postium.ru/promt-dlya-foto-v-stile-gta-6/) (16.11.2026)
- [Directline – 20 промптов для фото в стиле ГТА](https://www.directline.pro/connect/p/prompt-dlya-foto-v-stile-gta/)
- [Telegram «Дизайнерская бытовуха»](https://t.me/s/disignbit/625)
- [Lorka AI – GTA AI filter prompts](https://www.lorka.ai/knowledge-hub/gta-ai-filter-prompts)
- [Media.io – ChatGPT GTA 6 poster prompts](https://www.media.io/image-effects/chatgpt-gta-style-poster-prompts.html), [Media.io – GTA 6 loading screen](https://www.media.io/ai/explore/zone/gta-6-loading-screen-ai-generator)
- [YouMind: identity](https://youmind.com/prompts/gta-style-identity-transformation-33569), [retro Miami](https://youmind.com/prompts/retro-miami-character-poster-24174), [motorcycle](https://youmind.com/prompts/gta-vi-character-poster-28022), [beach club HUD](https://youmind.com/prompts/gta-beach-club-gameplay-14400), [dialogue](https://youmind.com/prompts/gta-style-dialogue-screenshot-13890), [open-world mockup](https://youmind.com/prompts/open-world-game-screenshot-mockup-14273), [crossover cover](https://youmind.com/prompts/gta-v-style-crossover-cover-art-13555), [San Andreas Indonesia](https://youmind.com/prompts/gta-san-andreas-indonesian-poster-26846), [Shinjuku](https://youmind.com/prompts/gta-6-shinjuku-bar-scene-15956)
- [Carat: 8511 Vice City 2026](https://carat.im/en/prompt-gallery/p/8511), [622](https://carat.im/en/prompt-gallery/p/622), [541](https://carat.im/en/prompt-gallery/p/541), [24973](https://carat.im/en/prompt-gallery/p/24973)
- [God of Prompt – screenshot mockup](https://godofprompt.ai/prompt-library/video-game-screenshot-mockup-tropical-town)
- [OOMOL – Rugged Superstar](https://prompts.oomol.com/p/rugged-superstar-hero-illustration-884bb852)
- [Magic Hour – GTA6 template](https://magichour.ai/templates/details/cmqxha4gp01slgh0z1unhruv3-gta6)
- [Perfect Corp / YouCam](https://www.perfectcorp.com/consumer/blog/generative-AI/gta-filter), [Pincel](https://blog.pincel.app/gta-style/), [Pixpretty](https://pixpretty.tenorshare.ai/ai-insights/gta-style-ai-prompt.html), [Analytics Insight](https://www.analyticsinsight.net/gaming/how-to-turn-your-images-into-gta-6-art-using-ai-chatgpt-gemini-and-more), [Ai Prompts and Tips](https://aipromptsandtips21.blogspot.com/2026/05/how-to-turn-yourself-into-gta-vi.html)
- [The Prompt Index – GTA](https://www.thepromptindex.com/image-database.php?style=GTA) (Midjourney, DALL-E)
- [WildVis / WildChat 1597614](https://wildvisualizer.com/conversation/wildchat/1597614) (Midjourney-шаблон)
- [Magica – 23 Midjourney prompts](https://magica.com/blog/midjourney-prompts-for-grand-theft-auto)
- [GTA Stylizer GPT – системный промт](https://github.com/LouisShark/chatgpt_system_prompt/blob/main/prompts/gpts/ostR6TTNg_GTA_Stylizer.md)
- Civitai (через открытый API, с метаданными картинок): [688840](https://civitai.com/models/688840), [66719](https://civitai.com/models/66719), [558832](https://civitai.com/models/558832), [119307](https://civitai.com/models/119307), [1551916](https://civitai.com/models/1551916), [525897](https://civitai.com/models/525897), [1111914](https://civitai.com/models/1111914), [2906696](https://civitai.com/models/2906696)
- Hugging Face: [WiroAI](https://huggingface.co/WiroAI/GTA6-style-flux-lora), [Castor](https://huggingface.co/prithivMLmods/Castor-Gta6-Theme-Flux-LoRA), [Pegasi](https://huggingface.co/prithivMLmods/Pegasi-Beta-GTA-LoRA), [GTA5 Artwork Diffusion](https://huggingface.co/ItsJayQz/GTA5_Artwork_Diffusion), [Motas](https://huggingface.co/Motas/GTA6), [FounderFeed](https://huggingface.co/FounderFeed/gta-style-lora)

Контекст и права:
- [Rockstar – Policy on posting copyrighted material](https://support.rockstargames.com/articles/200153756/Policy-on-posting-copyrighted-Rockstar-Games-material)
- [Лайфхакер – 20 обложек GTA, сделанных ChatGPT на Reddit](https://lifehacker.ru/gta-oblozhki-chatgpt/) (картинки без промтов)
- [Basic Apple Guy – GTA: Cupertino, Midjourney 5.2](https://basicappleguy.com/basicappleblog/grand-theft-auto-cupertino) (промты не опубликованы)

**Чего не нашлось**: готовых GTA-промтов под Ideogram и Leonardo; кода `--sref` под GTA; промта именно с надписью «Mission Passed»; живых тредов Reddit с промтами (Reddit и X без входа закрыты, в выдаче – только пересказы). Платные библиотеки (PromptBase) не открывали.
